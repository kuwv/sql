"""Demonstrate basic SQL statement."""

from typing import TYPE_CHECKING

import pytest

from sql import CREATE_DATABASE, CREATE_TABLE

# from sql import AND, END, EQ, FROM, CREATE_DATABASE, WHERE

if TYPE_CHECKING:
    from sqlite3 import Cursor


def test_create(cursor) -> None:
    """Test create statement."""
    statement = CREATE_DATABASE('Example').END()
    assert statement == 'CREATE DATABASE Example;'
    # cursor.execute(statement)


# def test_create_view() -> None:
#     """Test create statement."""
#     statement = (
#         CREATE_DATABASE()
#         .FROM(Example)
#         .WHERE(Example.TARGET)
#         .IN(':test1', ':test2')
#         .END()
#     )
#     # cursor.execute(statement)
#     assert statement == (
#         'CREATE_DATABASE * FROM Example '
#         + 'WHERE Example.TARGET '
#         + 'IN (:test1, :test2);'
#     )


def test_create_table(cursor: 'Cursor') -> None:
    """Test create statement."""
    statement = CREATE_TABLE(
        'users',
        (
            'PersonID int',
            'FirstName varchar(255)',
            'LastName varchar(255)',
            'Address varchar(255)',
            'City varchar(255)',
        ),
    ).END()
    assert statement == (
        'CREATE TABLE users ('
        + 'PersonID int, '
        + 'FirstName varchar(255), '
        + 'LastName varchar(255), '
        + 'Address varchar(255), '
        + 'City varchar(255)'
        + ');'
    )
    cursor.execute(statement)
    table = cursor.execute('PRAGMA table_info(users);')
    print(table.fetchone())
