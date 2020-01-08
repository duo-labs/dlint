# Dlint

[![Build Status](https://travis-ci.org/dlint-py/dlint.svg?branch=master)](https://travis-ci.org/dlint-py/dlint)
[![Coverage Status](https://coveralls.io/repos/github/dlint-py/dlint/badge.svg?branch=master)](https://coveralls.io/github/dlint-py/dlint?branch=master)
[![Python Versions](https://img.shields.io/pypi/pyversions/dlint.svg)](https://pypi.org/project/dlint/)
[![PyPI Version](https://img.shields.io/pypi/v/dlint.svg)](https://pypi.org/project/dlint/)

Dlint is a tool for encouraging best coding practices and helping ensure Python code is secure.

> The most important thing I have done as a programmer in recent years is to
> aggressively pursue static code analysis. Even more valuable than the
> hundreds of serious bugs I have prevented with it is the change in mindset
> about the way I view software reliability and code quality.
> - [John Carmack, 2011](https://www.gamasutra.com/view/news/128836/InDepth_Static_Code_Analysis.php)

> For a static analysis project to succeed, developers must feel they benefit
> from and enjoy using it.
> - [Lessons from Building Static Analysis Tools at Google](https://cacm.acm.org/magazines/2018/4/226371-lessons-from-building-static-analysis-tools-at-google/fulltext)

For documentation and a list of rules see [docs](https://github.com/duo-labs/dlint/tree/master/docs).

# Installing

```
$ python -m pip install dlint
```

*Specify `python2` or `python3` to install for a specific Python version.*

And double check that it was installed correctly:

```
$ python -m flake8 -h
Usage: flake8 [options] file file ...

...

Installed plugins: dlint: 0.9.2, mccabe: 0.5.3, pycodestyle: 2.2.0, pyflakes: 1.3.0
```

Note the `dlint: 0.9.2`.

# Using

Dlint uses `flake8` to perform its linting functionality which provides many
useful features without re-inventing the wheel.

## CLI

Let's run a simple check:

```
$ cat << EOF > test.py
print("TEST1")
exec('print("TEST2")')
EOF
```

```
$ python test.py
TEST1
TEST2
```

```
$ python -m flake8 --select=DUO test.py
test.py:2:1: DUO105 use of "exec" is insecure
```

*To learn more about why "exec" is insecure visit [`/docs/linters/DUO105.md`](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO105.md).*

The `--select=DUO` flag tells `flake8` to only run Dlint lint rules.

*Why `DUO`? Dlint was originally developed by the [Duo Labs](https://duo.com/blog/introducing-dlint-robust-static-analysis-for-python) team.*

From here, we can easily run Dlint against a directory of Python code:

```
$ python -m flake8 --select=DUO /path/to/code
```

To fine-tune your linting, check out the `flake8` help:

```
$ python -m flake8 --help
```

## Inline Editor

Dlint results can also be included inline in your editor for fast feedback.
This typically requires an editor plugin or extension. Here are some starting
points for common editors:

* Vim: [https://github.com/vim-syntastic/syntastic](https://github.com/vim-syntastic/syntastic)
* Emacs: [https://github.com/flycheck/flycheck](https://github.com/flycheck/flycheck)
* Sublime: [https://github.com/SublimeLinter/SublimeLinter-flake8](https://github.com/SublimeLinter/SublimeLinter-flake8)
* PyCharm: [https://foxmask.net/post/2016/02/17/pycharm-running-flake8/](https://foxmask.net/post/2016/02/17/pycharm-running-flake8/)
* Atom: [https://atom.io/packages/linter-flake8](https://atom.io/packages/linter-flake8)
* Visual Studio Code: [https://code.visualstudio.com/docs/python/linting#_flake8](https://code.visualstudio.com/docs/python/linting#_flake8)

# Integrating

Dlint can easily be integrated into CI pipelines, or anything really.

For more information and examples see ['How can I integrate Dlint into XYZ?'](https://github.com/duo-labs/dlint/tree/master/docs#how-can-i-integrate-dlint-into-xyz).

# Custom Plugins

Dlint's custom plugins are built on a [simple naming convention](https://packaging.python.org/guides/creating-and-discovering-plugins/#using-naming-convention),
and rely on [Python modules](https://docs.python.org/3/distutils/examples.html#pure-python-distribution-by-module).
To make a Dlint custom plugin use the following conventions:

* The Python module name **must** start with `dlint_plugin_`.
* The linter class name **must** start with `Dlint`.
* The linter class **should** inherit from `dlint.linters.base.BaseLinter`.
  * If for some reason you'd like to avoid this, then you **must** implement
	the `get_results` function appropriately and inherit from `ast.NodeVisitor`.

See an [example plugin](https://github.com/duo-labs/dlint-plugin-example) for further details.

# Developing

First, install development packages:

```
$ python -m pip install -r requirements.txt
$ python -m pip install -r requirements-dev.txt
$ python -m pip install -e .
```

## Testing

```
$ pytest
```

## Linting

```
$ flake8
```

## Coverage

```
$ pytest --cov
```

## Benchmarking

```
$ pytest --benchmark-py-file /path/to/python/file tests/test_benchmark/
```
