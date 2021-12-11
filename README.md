# Template Python Project [![Pipeline](https://github.com/limazix/template-python-project/actions/workflows/main.yml/badge.svg)](https://github.com/limazix/template-python-project/actions/workflows/main.yml) [![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)

### Requirements

- [Python](https://python.org) **(v3.7+)**
- [Poetry](https://python-poetry.org/) **(v1.1+)**
- [Makefile](https://makefiletutorial.com/)

### Documentation

The API documentation will be automatically generated on deploy stage at master merge operation by the CI tool. It uses the package [Lazydocs](https://pypi.org/project/lazydocs/) to convert all Docstrings from the scripts at tools folder to Markdown and store the output into docs folder. After, it uses package [Mkdocs](https://www.mkdocs.org/) to generate the static site and publish it as a Github page.

## Usage

### Rename

The first step to use this repository is tochange the names and paths from the following files:
- README.md
- Makefile
- mkdocs.yml
- pyproject.toml

### Tests

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
