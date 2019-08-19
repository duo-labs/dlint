# Docs

Dlint uses a simple, folder-based hierarchy written in [Markdown](https://en.wikipedia.org/wiki/Markdown) for documentation.

# Linters

* [DUO101](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO101.md)
* [DUO102](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO102.md)
* [DUO103](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO103.md)
* [DUO104](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO104.md)
* [DUO105](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO105.md)
* [DUO106](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO106.md)
* [DUO107](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO107.md)
* [DUO108](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO108.md)
* [DUO109](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO109.md)
* [DUO110](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO110.md)
* [DUO111](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO111.md)
* [DUO112](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO112.md)
* [DUO113](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO113.md)
* [DUO114](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO114.md)
* [DUO115](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO115.md)
* [DUO116](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO116.md)
* [DUO117](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO117.md)
* [DUO118](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO118.md)
* [DUO119](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO119.md)
* [DUO120](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO120.md)
* [DUO121](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO121.md)
* [DUO122](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO122.md)
* [DUO123](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO123.md)
* [DUO124](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO124.md)
* [DUO125](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO125.md)
* [DUO126](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO126.md)
* [DUO127](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO127.md)
* [DUO128](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO128.md)
* [DUO129](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO129.md)
* [DUO130](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO130.md)
* [DUO131](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO131.md)
* [DUO132](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO132.md)

# FAQs

## Why not Bandit?

[Bandit](https://bandit.readthedocs.io/en/latest/) is another static analysis
tool aimed at searching for security issues in Python code. Bandit is a great
tool and can easily be used simultaneously with Dlint. However, there are a few
advantages Dlint has over Bandit:

* Dlint can identify function calls that are insecure specifically because of
their keyword argument usage. For example, `subprocess` module function calls
that use the `shell=True` keyword argument:
[`subprocess` security considerations](https://docs.python.org/3/library/subprocess.html#security-considerations).
* Dlint can identify insecure method calls on specific objects. For example,
the [`TarFile.extractall`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall)
object method can often lead to security vulnerabilities. Dlint tracks variable
names of instantiated objects and searches for insecure methods used by these
specific objects.
* Dlint is built upon the ubiquitous [Flake8](https://flake8.pycqa.org/en/latest/)
project so it's easy to use, provides a fully-featured interface, and is backed
by the [Python Code Quality Authority](https://github.com/PyCQA). This means
things like no more re-inventing the wheel for
[selecting and ignoring violations](https://flake8.pycqa.org/en/latest/user/violations.html),
[including and excluding specific files](https://flake8.pycqa.org/en/latest/user/invocation.html),
[running multiple jobs in parallel](https://flake8.pycqa.org/en/latest/user/options.html#cmdoption-flake8-jobs),
and much more.

Running multiple security tools over your codebase will provide a more
comprehensive analysis and ensure you're coding with confidence.
