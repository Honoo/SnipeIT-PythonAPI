
# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [1.0.0] - 2024-01-09

### Added

### Changed
- In `Assets.py`, consolidate redundant code in `getAsset...` functions to create a request and call the Snipe-IT server into one function.
- For builds: stop using `setup.py`, which is deprecated, and switch to `pyproject.toml`.

### Fixed
- In `Assets::getAssetsByModel()`, actually use the model ID parameter when making the request.