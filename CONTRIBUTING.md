# Contributing

`Dlint` welcomes contributions from anyone. If you have an idea for a linter
but don't know how to implement one please [create a new issue](https://github.com/dlint-py/dlint/issues).
With `dlint` we can find security bugs, encourage best practices, and eliminate
anti-patterns across the Python ecosystem.

`Dlint` is built on top of Python's [AST](https://docs.python.org/3/library/ast.html)
module and the [`flake8` plugin system](http://flake8.pycqa.org/en/latest/user/using-plugins.html).
It may be helpful to review those systems before beginning `dlint` development,
but `dlint` aims to be easily extendable without requiring a lot of background
knowledge. **Further, please check out our brief section on [developing](https://github.com/dlint-py/dlint#developing)
`dlint` before making changes.**

# New Linters

When adding new linters:

* New linters should be added to the `dlint/linters/` directory.
* Add a new file and class inheriting from `base.BaseLinter` for each new linter.
* Add a "pass-through" import of the new class to `dlint.linters.__init__.py`.
* Add the new class to `ALL` in `dlint.linters.__init__.py`.
* Add documentation link in `docs/README.md`.
* Add documentation file in `docs/linters/`.
* Ensure new rules are properly tested (high or complete test coverage).
* Ensure new code adheres to the style guide/linting process.
* Add new rule information to `CHANGELOG.md` under `Unreleased` section, `Added` sub-section.

From here, please create a [pull request](https://github.com/dlint-py/dlint/pulls)
with your changes and wait for a review.

# Fixing/Reporting Bugs

When fixing or reporting bugs in `dlint` please [create a new issue](https://github.com/dlint-py/dlint/issues)
first. This issue should include a snippet of code for reproducing the bug.

E.g.

*I expected `dlint` to flag the following code for faulty use of the `foo` module:*

```
from bar import foo

var = result + 7
widget = foo.baz(var)
send_result(widget)
```

*Please update `dlint` to catch this. Thanks!*

After reporting the issue, if you'd like to help fix it, please create a
[pull request](https://github.com/dlint-py/dlint/pulls) with the
fix applied and wait for a review.
