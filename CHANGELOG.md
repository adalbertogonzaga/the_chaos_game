# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). An `Unreleased` section is allowed when changes are being merged but not released yet.

Types of changes: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed` and `Security`.

[//]: # (The latest version must start on line 9. The GitHub Actions of this repo rely on it. You ca use UNRELEASED as the version if you don't want to release.)
## [0.3.0-alpha]
### Added
- CHANGELOG.md
- `pull_request.yml` action to check PRs for a CHANGELOG.md modification (and potentially lint and test the files later?)
- `release.yml` action to automatically release upon merge on `main` branch.

## [0.2-alpha]
### Fixed
- Fix the score to update on every iteration. 

## [0.1-alpha]
### Added
- The basics.