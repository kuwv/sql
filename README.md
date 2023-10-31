# sql
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://spdx.org/licenses/MIT)
![Build Status](https://github.com/kuwv/sql/actions/workflows/main.yml/badge.svg?branch=master)
[![codecov](https://codecov.io/gh/kuwv/sql/branch/master/graph/badge.svg)](https://codecov.io/gh/kuwv/sql)

## Overview

Python SQL

## Install

```
pip install sql
```

## Development

```
podman pull postges:latest
podman run --name postgres -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres

```

```
pip install --user virtualenv
virtualenv .env
source .env/bin/activate
pip install -e .[dev]
```

## References

- https://peps.python.org/pep-0292/
- https://peps.python.org/pep-3101/  # depracted
