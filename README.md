# SMTR: Data Engineering Challenge [![Pipeline](https://github.com/limazix/smtr-data-engineering-challenge/actions/workflows/main.yml/badge.svg)](https://github.com/limazix/smtr-data-engineering-challenge/actions/workflows/main.yml) [![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)

## <a id="overview"/> Overview

This project aims to help the SMTR challenge for data engineering on buses data lake pipeline modeling and creation.

### <a id="requirements"/> Requirements

- [Python](https://python.org) **(v3.7+)**
- [Poetry](https://python-poetry.org/) **(v1.1+)**
- [Makefile](https://makefiletutorial.com/)

### <a id="documentation"/> Documentation

The API documentation will be automatically generated on deploy stage at master merge operation by the CI tool. It uses the package [Lazydocs](https://pypi.org/project/lazydocs/) to convert all Docstrings from the scripts at tools folder to Markdown and store the output into docs folder. After, it uses package [Mkdocs](https://www.mkdocs.org/) to generate the static site and publish it as a Github page.

## <a id="usage"/> Usage

### <a id="tests"/> Tests

Run tests only one time
```sh
make test
```

Run tests with watch function enabled
```sh
make test-watch
```

### <a id="commits"/> Commits

This project uses the [Semantic Version](http://semver.org) pattern to generate the package release and it changelogs. To make it work properly, it implement a different flow of actions for commits.


```sh
make commit # start the commit pipeline
```

The commit pipeline is supported by the [Commitizen](https://commitizen-tools.github.io/commitizen/) module. The first one is a cli tool that guide the devloper through the commit pipeline by inquiring for what need to be done. And the second one check if the generated commit follows the [Semantic Version](http://semver.org) pattern.
