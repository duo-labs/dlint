# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Support for Python 3.8 ([#12](https://github.com/duo-labs/dlint/issues/12))
- `DUO134`: lint for insecure cryptography usage ([#6](https://github.com/duo-labs/dlint/issues/6))
- `DUO135`: lint for insecure defusedxml usage ([#5](https://github.com/duo-labs/dlint/issues/5))

### Fixed
- False negative when deep imports are not fully specified in bad module attribute ([#1](https://github.com/duo-labs/dlint/issues/1))
- False negative - consider 'async' functions in bad name attribute (7bd249e80a91f7c38f2c1f05045a826e0bef3246)

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
