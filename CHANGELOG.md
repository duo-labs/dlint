# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
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
