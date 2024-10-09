# sentier_peakachu

[![PyPI](https://img.shields.io/pypi/v/sentier_peakachu.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/sentier_peakachu.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/sentier_peakachu)][pypi status]
[![License](https://img.shields.io/pypi/l/sentier-peakachu)][license]

[![Read the documentation at https://sentier-peakachu.readthedocs.io/](https://img.shields.io/readthedocs/sentier_peakachu/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/TimoDiepers/sentier_peakachu/actions/workflows/python-test.yml/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/TimoDiepers/sentier-peakachu/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/sentier.peakachu/
[read the docs]: https://sentier-peakachu.readthedocs.io/
[tests]: https://github.com/TimoDiepers/sentier_peakachu/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/TimoDiepers/sentier_peakachu
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

This is a repo for the group work at the DdS Autumn School 2024, working on the integration of electricity markets.

## Installation

You can install _sentier_peakachu_ via [pip] from [PyPI]:

```console
$ pip install sentier_peakachu
```

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide][Contributor Guide].

## License

Distributed under the terms of the [BSD 3 Clause license][License],
_sentier_peakachu_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue][Issue Tracker] along with a detailed description.

<!-- github-only -->

[command-line reference]: https://sentier_peakachu.readthedocs.io/en/latest/usage.html
[License]: https://github.com/TimoDiepers/sentier_peakachu/blob/main/LICENSE
[Contributor Guide]: https://github.com/TimoDiepers/sentier_peakachu/blob/main/CONTRIBUTING.md
[Issue Tracker]: https://github.com/TimoDiepers/sentier_peakachu/issues

## Building the Documentation

You can build the documentation locally by installing the documentation Conda environment:

```bash
conda env create -f docs/environment.yml
```

activating the environment

```bash
conda activate sphinx_sentier_peakachu
```

and [running the build command](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#sphinx-build):

```bash
sphinx-build docs _build/html --builder=html --jobs=auto --write-all; open _build/html/index.html
```
