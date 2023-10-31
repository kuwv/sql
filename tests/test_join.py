"""Demonstrate basic SQL statement."""
from enum import Enum, auto

from sql import EQ, SELECT

# from sql import AND, END, EQ, FROM, SELECT, WHERE


class Example(Enum):
    """Provide exmample schema object."""

    NAME = auto()
    TARGET = auto()


def test_inner_join() -> None:
    """Test select statement."""
    statement = (
        SELECT('columns')
        .FROM('table1')
        .INNER_JOIN('table2')
        .ON('table1.column' | EQ | 'table2.column')
        .END()
    )
    # cursor.execute(statement)
    assert statement == (
        'SELECT columns '
        + 'FROM table1 '
        + 'INNER JOIN table2 '
        + 'ON table1.column = table2.column;'
    )


def test_left_join() -> None:
    """Test select statement."""
    statement = (
        SELECT('columns')
        .FROM('table1')
        .LEFT_JOIN('table2')
        .ON('table1.column' | EQ | 'table2.column')
        .END()
    )
    # cursor.execute(statement)
    assert statement == (
        'SELECT columns '
        + 'FROM table1 '
        + 'LEFT JOIN table2 '
        + 'ON table1.column = table2.column;'
    )


def test_right_join() -> None:
    """Test select statement."""
    statement = (
        SELECT('columns')
        .FROM('table1')
        .RIGHT_JOIN('table2')
        .ON('table1.column' | EQ | 'table2.column')
        .END()
    )
    # cursor.execute(statement)
    assert statement == (
        'SELECT columns '
        + 'FROM table1 '
        + 'RIGHT JOIN table2 '
        + 'ON table1.column = table2.column;'
    )


def test_full_join() -> None:
    """Test select statement."""
    statement = (
        SELECT('columns')
        .FROM('table1')
        .FULL_JOIN('table2')
        .ON('table1.column' | EQ | 'table2.column')
        .END()
    )
    # cursor.execute(statement)
    assert statement == (
        'SELECT columns '
        + 'FROM table1 '
        + 'FULL JOIN table2 '
        + 'ON table1.column = table2.column;'
    )
