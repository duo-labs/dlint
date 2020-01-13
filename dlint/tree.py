#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import ast
import sys


def decorator_name(decorator):
    if isinstance(decorator, ast.Attribute):
        # E.g. @module.decorator
        return decorator.attr
    elif isinstance(decorator, ast.Name):
        # E.g. @decorator
        return decorator.id
    elif isinstance(decorator, ast.Call):
        if isinstance(decorator.func, ast.Attribute):
            # E.g. @module.decorator(argument)
            return decorator.func.attr
        elif isinstance(decorator.func, ast.Name):
            # E.g. @decorator(argument)
            return decorator.func.id
    else:
        raise TypeError('expected type ast.Attribute, ast.Name, or ast.Call, received {}'.format(type(decorator)))


def function_has_inlinecallbacks_decorator(function):
    return any(
        decorator_name(decorator) == 'inlineCallbacks'
        for decorator in function.decorator_list
    )


def function_is_empty(function):
    def raise_or_pass_or_docstring(node):
        return (
            isinstance(node, ast.Raise)
            or isinstance(node, ast.Pass)
            or (isinstance(node, ast.Expr) and isinstance(node.value, ast.Str))
        )

    return all(
        raise_or_pass_or_docstring(child)
        for child in function.body
    )


def call_is_returnvalue(call):
    if isinstance(call, ast.Attribute):
        if isinstance(call.value, ast.Name):
            # E.g. defer.returnValue(argument)
            return (
                call.value.id == 'defer'
                and call.attr == 'returnValue'
            )
        else:
            # E.g. foo(argument).bar()
            return False
    elif isinstance(call, ast.Name):
        # E.g. returnValue(argument)
        return call.id == 'returnValue'
    else:
        # E.g. foo(argument).bar()()
        return False


def non_empty_return(_return):
    return _return.value is not None


def walk_callback_same_scope(node, callback):
    is_python_3_5 = sys.version_info >= (3, 5)

    # If we change scope, e.g. enter into a new
    # class or function definition, then halt iteration
    scopes = (ast.ClassDef, ast.FunctionDef)
    if is_python_3_5:
        scopes += (ast.AsyncFunctionDef,)

    def scope_predicate(inner_node):
        return not isinstance(inner_node, scopes)

    walk_callback(node, callback, predicate=scope_predicate)


def walk_callback(node, callback, predicate=lambda n: True):
    for child_node in ast.iter_child_nodes(node):
        if not predicate(child_node):
            continue

        callback(child_node)
        walk_callback(child_node, callback, predicate=predicate)


def kwarg_present(call, kwarg_name):
    return kwarg_name in (keyword.arg for keyword in call.keywords)


def kwarg_not_present(call, kwarg_name):
    return not kwarg_present(call, kwarg_name)


def kwarg_primitive(call, kwarg_name, primitive):
    try:
        # Python 3
        primitive_type = ast.NameConstant

        def comparator(keyword, inner_primitive):
            return (
                isinstance(keyword.value, primitive_type)
                and keyword.value.value == inner_primitive
            )
    except AttributeError:
        # Python 2, AttributeError on ast.NameConstant
        primitive_type = ast.Name

        def comparator(keyword, inner_primitive):
            return (
                isinstance(keyword.value, primitive_type)
                and keyword.value.id == str(inner_primitive)
            )

    return any(
        keyword.arg == kwarg_name
        and comparator(keyword, primitive)
        for keyword in call.keywords
    )


def kwarg_false(call, kwarg_name):
    return kwarg_primitive(call, kwarg_name, False)


def kwarg_true(call, kwarg_name):
    return kwarg_primitive(call, kwarg_name, True)


def kwarg_none(call, kwarg_name):
    return kwarg_primitive(call, kwarg_name, None)


def kwarg_str(call, kwarg_name, s):
    return any(
        keyword.arg == kwarg_name
        and isinstance(keyword.value, ast.Str)
        and keyword.value.s == s
        for keyword in call.keywords
    )


def kwarg_module_path(call, kwarg_name, illegal_module_path, namespace):
    return any(
        keyword.arg == kwarg_name
        and isinstance(keyword.value, (ast.Attribute, ast.Name))
        and namespace.illegal_module_imported(
            module_path_str(keyword.value),
            illegal_module_path
        )
        for keyword in call.keywords
    )


def kwarg_module_path_call(call, kwarg_name, illegal_module_path, namespace):
    return any(
        keyword.arg == kwarg_name
        and isinstance(keyword.value, ast.Call)
        and isinstance(keyword.value.func, (ast.Attribute, ast.Name))
        and namespace.illegal_module_imported(
            module_path_str(keyword.value.func),
            illegal_module_path
        )
        for keyword in call.keywords
    )


def kwarg_any(kwarg_functions):
    """Resolve kwarg predicates with short-circuit evaluation. This optimization
    technique means we do not have to evaluate every predicate if one is already
    true.
    """
    return any(kwarg_function() for kwarg_function in kwarg_functions)


def module_path(node):
    """Recursively walk up a series of node attributes.
    E.g. if we have foo.bar.baz, iterate baz -> bar -> foo.
    """
    if isinstance(node, ast.Attribute):
        return module_path(node.value) + [node.attr]
    elif isinstance(node, ast.Name):
        return [node.id]
    else:
        return []


def module_path_str(node):
    """Return module path as a string instead of a list.
    E.g. "foo.bar.baz" instead of ["foo", "bar", "baz"].
    """
    return ".".join(module_path(node))


def same_modules(s1, s2):
    """Compare two module strings where submodules of an illegal
    parent module should also be illegal. I.e. blacklisting 'foo.bar'
    should also make 'foo.bar.baz' illegal.

    The first argument should 'encompass' the second, not the other way
    around. I.e. passing same_modules('foo', 'foo.bar') will return True,
    but same_modules('foo.bar', 'foo') will not.
    """
    modules1 = s1.split(".")
    modules2 = s2.split(".")

    return (
        len(modules1) <= len(modules2)
        and all(m1 == m2 for (m1, m2) in zip(modules1, modules2))
    )
