# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- `DUO137`: lint for insecure itsdangerous kwarg usage ([#36](https://github.com/duo-labs/dlint/issues/36))

### Fixed
- False positive for `DUO137`. ([#39](https://github.com/duo-labs/dlint/issues/39))

## [0.9.2] - 2019-11-21
### Fixed
- False negative with arbitrary depth from import alias in bad module attribute ([#32](https://github.com/duo-labs/dlint/issues/32))
- False negative with arbitrary depth from import wildcard in bad module attribute ([#33](https://github.com/duo-labs/dlint/issues/33))

## [0.9.1] - 2019-11-06
### Fixed
- False positive with `input` as variable name ([#31](https://github.com/duo-labs/dlint/issues/31))

## [0.9.0] - 2019-10-13
### Added
- `DUO116`: rule for `subprocess.run` ([#24](https://github.com/duo-labs/dlint/issues/24))
- The `--print-dlint-linters` command-line flag to print all Dlint linters ([#26](https://github.com/duo-labs/dlint/issues/26))
- `DUO136`: lint for insecure xmlsec usage ([#27](https://github.com/duo-labs/dlint/issues/27))

### Changed
- Visitor strategy to minimize node visits - ~25% speed up ([#28](https://github.com/duo-labs/dlint/issues/28))

### Fixed
- False negative with nested imports in bad module attribute ([#30](https://github.com/duo-labs/dlint/issues/30))

### Removed
- `dlint.linters.helpers.bad_kwarg_use`: use of `attribute_name` in favor of fully specified `module_path` ([#19](https://github.com/duo-labs/dlint/issues/19))
- `dlint.tree`: use of `kwarg_attribute` in favor of `kwarg_module_path` ([#21](https://github.com/duo-labs/dlint/issues/21))
- `dlint.linters.helpers.bad_name_attribute_use`: use of attribute list in favor of fully specified module path ([#20](https://github.com/duo-labs/dlint/issues/20))

## [0.8.0] - 2019-09-18
### Added
- Support for Python 3.8 ([#12](https://github.com/duo-labs/dlint/issues/12))
- `DUO134`: lint for insecure cryptography usage ([#6](https://github.com/duo-labs/dlint/issues/6))
- `DUO135`: lint for insecure defusedxml usage ([#5](https://github.com/duo-labs/dlint/issues/5))

### Deprecated
- `dlint.linters.helpers.bad_kwarg_use`: use of `attribute_name` in favor of fully specified `module_path` ([#19](https://github.com/duo-labs/dlint/issues/19))
- `dlint.tree`: use of `kwarg_attribute` in favor of `kwarg_module_path` ([#21](https://github.com/duo-labs/dlint/issues/21))
- `dlint.linters.helpers.bad_name_attribute_use`: use of attribute list in favor of fully specified module path ([#20](https://github.com/duo-labs/dlint/issues/20))

### Fixed
- False negative when deep imports are not fully specified in bad module attribute ([#1](https://github.com/duo-labs/dlint/issues/1))
- False negative - consider `async` functions in bad name attribute ([7bd249e](https://github.com/duo-labs/dlint/commit/7bd249e80a91f7c38f2c1f05045a826e0bef3246))
- False negative in various import scenarios when using `attribute_name` in bad kwarg ([#19](https://github.com/duo-labs/dlint/issues/19))
- False negative in various import scenarios when using `kwarg_attribute` in bad kwarg ([#21](https://github.com/duo-labs/dlint/issues/21))
- False negative in various import scenarios when using attribute list in bad name attribute ([#20](https://github.com/duo-labs/dlint/issues/20))

## [0.7.0] - 2019-08-24
### Added
- `DUO133`: lint for pycrypto usage ([#7](https://github.com/duo-labs/dlint/issues/7))

### Fixed
- False positive when bad builtin is overwritten by import ([#16](https://github.com/duo-labs/dlint/issues/16))
- False negative when bad module attribute uses import alias ([#2](https://github.com/duo-labs/dlint/issues/2))
- False positive when bad module attribute not imported ([#14](https://github.com/duo-labs/dlint/issues/14))

## [0.6.0] - 2019-08-12
### Added
- Support for Python 3.5 and 3.7 ([#9](https://github.com/duo-labs/dlint/issues/9))
- `DUO131`: lint for disabling urllib3 warnings
- `DUO132`: lint for disabling urllib3 HTTPS certification verification

### Removed
- `FormatStringLinter`, previously `DUO104`, as it was a disabled expirement ([#15](https://github.com/duo-labs/dlint/issues/15))

## [0.5.0] - 2019-07-17
### Added
- Initial public release of Dlint
