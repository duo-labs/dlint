# Docs

Dlint uses a simple, folder-based hierarchy written in [Markdown](https://en.wikipedia.org/wiki/Markdown) for documentation.

# Linters

* [`DUO101` `YieldReturnStatementLinter` "inlineCallbacks" function cannot have non-empty "return" statement](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO101.md)
* [`DUO102` `BadRandomGeneratorUseLinter` insecure use of "random" module, prefer "random.SystemRandom"](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO102.md)
* [`DUO103` `BadPickleUseLinter` insecure use of "pickle" or "cPickle"](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO103.md)
* [`DUO104` `BadEvalUseLinter` use of "eval" is insecure](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO104.md)
* [`DUO105` `BadExecUseLinter` use of "exec" is insecure](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO105.md)
* [`DUO106` `BadOSUseLinter` insecure use of "os" module](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO106.md)
* [`DUO107` `BadXMLUseLinter` insecure use of XML modules, prefer "defusedxml"](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO107.md)
* [`DUO108` `BadInputUseLinter` use of "input" is insecure](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO108.md)
* [`DUO109` `BadYAMLUseLinter` insecure use of "yaml" parsing function, prefer "safe_*" equivalent](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO109.md)
* [`DUO110` `BadCompileUseLinter` use of "compile" is insecure](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO110.md)
* [`DUO111` `BadSysUseLinter` insecure use of "sys" module](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO111.md)
* [`DUO112` `BadZipfileUseLinter` use of "extract|extractall" is insecure](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO112.md)
* [`DUO113` `InlineCallbacksYieldStatementLinter` "inlineCallbacks" function missing "yield" statement](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO113.md)
* [`DUO114` `ReturnValueInInlineCallbacksLinter` "returnValue" in function missing "inlineCallbacks" decorator](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO114.md)
* [`DUO115` `BadTarfileUseLinter` use of "extract|extractall" is insecure](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO115.md)
* [`DUO116` `BadSubprocessUseLinter` use of "shell=True" is insecure in "subprocess" module](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO116.md)
* [`DUO117` `BadDlUseLinter` avoid "dl" module use](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO117.md)
* [`DUO118` `BadGlUseLinter` avoid "gl" module use](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO118.md)
* [`DUO119` `BadShelveUseLinter` avoid "shelve" module use](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO119.md)
* [`DUO120` `BadMarshalUseLinter` avoid "marshal" module use](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO120.md)
* [`DUO121` `BadTempfileUseLinter` use of "tempfile.mktemp" allows for race conditions](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO121.md)
* [`DUO122` `BadSSLModuleAttributeUseLinter` insecure "ssl" module attribute use](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO122.md)
* [`DUO123` `BadRequestsUseLinter` use of "verify=False" is insecure in "requests" module](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO123.md)
* [`DUO124` `BadXmlrpcUseLinter` instance with "allow_dotted_names" enabled is insecure](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO124.md)
* [`DUO125` `BadCommandsUseLinter` avoid "commands" module use](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO125.md)
* [`DUO126` `BadPopen2UseLinter` avoid "popen2" module use](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO126.md)
* [`DUO127` `BadDuoClientUseLinter` use of "ca_certs=HTTP|DISABLE" is insecure in "duo_client" module](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO127.md)
* [`DUO128` `BadOneLoginKwargUseLinter` insecure "OneLogin" SAML function call](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO128.md)
* [`DUO129` `BadOneLoginModuleAttributeUseLinter` insecure "OneLogin" SAML attribute use](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO129.md)
* [`DUO130` `BadHashlibUseLinter` insecure use of "hashlib" module](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO130.md)
* [`DUO131` `BadUrllib3ModuleAttributeUseLinter` "urllib3" warnings disabled, insecure connections possible](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO131.md)
* [`DUO132` `BadUrllib3KwargUseLinter` "urllib3" certificate verification disabled, insecure connections possible](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO132.md)
* [`DUO133` `BadPycryptoUseLinter` use of "Crypto" module is insecure](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO133.md)
* [`DUO134` `BadCryptographyModuleAttributeUseLinter` insecure "cryptography" attribute use](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO134.md)
* [`DUO135` `BadDefusedxmlUseLinter` enable all "forbid_*" defenses when using "defusedxml" parsing](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO135.md)
* [`DUO136` `BadXmlsecModuleAttributeUseLinter` insecure "xmlsec" attribute use](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO136.md)
* [`DUO137` `BadItsDangerousKwargUseLinter` insecure "itsdangerous" use allowing empty signing](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO137.md)
* [`DUO138` `BadReCatastrophicUseLinter` catastrophic "re" usage - denial-of-service possible](https://github.com/duo-labs/dlint/blob/master/docs/linters/DUO138.md)

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
* Dlint can identify insecurities arising from the use of wildcard imports. For
example, `from os import *`, which results in insecure use of the `os` module,
such as a `system` call.
* Dlint is built upon the ubiquitous [Flake8](https://flake8.pycqa.org/en/latest/)
project so it's easy to use, provides a fully-featured interface, and is backed
by the [Python Code Quality Authority](https://github.com/PyCQA). This means
things like no more re-inventing the wheel for
[selecting and ignoring violations](https://flake8.pycqa.org/en/latest/user/violations.html),
[including and excluding specific files](https://flake8.pycqa.org/en/latest/user/invocation.html),
[running multiple jobs in parallel](https://flake8.pycqa.org/en/latest/user/options.html#cmdoption-flake8-jobs),
[showing results inline in your editor](https://github.com/duo-labs/dlint#inline-editor),
and much more.

Bandit also provides some advantages over Dlint:

* Bandit can identify SQL injections in your code: [B608](https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html).
* Bandit can identify security issues resulting from hardcoded information:
[B104](https://bandit.readthedocs.io/en/latest/plugins/b104_hardcoded_bind_all_interfaces.html),
[B105](https://bandit.readthedocs.io/en/latest/plugins/b105_hardcoded_password_string.html),
[B106](https://bandit.readthedocs.io/en/latest/plugins/b106_hardcoded_password_funcarg.html),
[B107](https://bandit.readthedocs.io/en/latest/plugins/b107_hardcoded_password_funcdef.html), and
[B108](https://bandit.readthedocs.io/en/latest/plugins/b108_hardcoded_tmp_directory.html).

Running multiple security tools over your codebase will provide a more
comprehensive analysis and ensure you're coding with confidence.

## Where can I learn more about static analysis?

* [Lessons from Building Static Analysis Tools at Google (2018)](https://cacm.acm.org/magazines/2018/4/226371-lessons-from-building-static-analysis-tools-at-google/fulltext)
* [Scaling Static Analyses at Facebook (2019)](https://cacm.acm.org/magazines/2019/8/238344-scaling-static-analyses-at-facebook/fulltext)
* [Static Analysis at Scale: An Instagram Story (2019)](https://instagram-engineering.com/static-analysis-at-scale-an-instagram-story-8f498ab71a0c)
* [A Few Billion Lines of Code Later: Using Static Analysis to Find Bugs in the Real World (2010)](https://cacm.acm.org/magazines/2010/2/69354-a-few-billion-lines-of-code-later/fulltext)
* [How to Build Static Checking Systems Using Orders of Magnitude Less Code (2016)](https://web.stanford.edu/~mlfbrown/paper.pdf)
* [What Developers Want and Need from Program Analysis: An Empirical Study (2016)](https://www.microsoft.com/en-us/research/publication/what-developers-want-and-need-from-program-analysis-an-empirical-study/)

## How can I integrate Dlint into XYZ?

### TravisCI

Include Dlint in your `.travis.yml` configuration file:

```
language: python
install:
    - python -m pip install dlint
script:
    - python -m flake8 --select=DUO /path/to/code
```

### CircleCI

Include Dlint in your `.circleci/config.yml` configuration file:

```
version: 2
jobs:
    build:
        docker:
            - image: circleci/python
        steps:
            - checkout
            - run: python -m pip install dlint
            - run: python -m flake8 --select=DUO /path/to/code
```

### Gitlab

Include Dlint in your `.gitlab-ci.yml` configuration file:

```
stages:
    - test
test:
    image: python
    before_script:
        - python -m pip install dlint
    script:
        - python -m flake8 --select=DUO /path/to/code
```

### Phabricator

Include Dlint in your [Arcanist](https://secure.phabricator.com/book/phabricator/article/arcanist/)
linting process via the [`.arclint`](https://secure.phabricator.com/book/phabricator/article/arcanist_lint/)
configuration file:
```
{
    "linters": {
        "sample": {
            "type": "flake8"
        }
    }
}
```

Dlint rules will automatically be run via `flake8` once it's installed, so the
standard `flake8` configuration will work. You can also utilize more granular
control over the linting process:

```
{
    "linters": {
        "sample": {
            "type": "flake8"
        },
        "bin": ["python2.7", "python2"],
        "flags": ["-m", "flake8", "--select", "DUO"]
    }
}
```

## How can I output results in JSON?

Use the [`flake8-json`](https://gitlab.com/pycqa/flake8-json) plugin:

```
$ python -m pip install flake8-json
```

```
$ python -m flake8 --format=json --select=DUO ...
```
