# sql
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://spdx.org/licenses/MIT)
![Build Status](https://github.com/kuwv/sql/actions/workflows/main.yml/badge.svg?branch=master)
[![codecov](https://codecov.io/gh/kuwv/sql/branch/master/graph/badge.svg)](https://codecov.io/gh/kuwv/sql)

## Overview

This library is a SQL implementation in Python to provide safe parameterized queries. It is inspired from jOOQ.

## Install

```
pip install sql
```

## Perform `select` query.

```
>>> from sql import AND, EQ, SELECT

>>> SELECT()\
... .FROM('Example')\
... .WHERE(
...     ('Example.NAME' | EQ | '?')
...     | AND
...     | ('Example.TARGET' | EQ | '?')
... )\
... .END()
'SELECT * FROM Example WHERE Example.NAME = ? AND Example.TARGET = ?;'

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
