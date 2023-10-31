"""Demonstrate basic SQL statement."""
from enum import Enum, auto

from sql import AND, EQ, SELECT

# from sql import AND, END, EQ, FROM, SELECT, WHERE


class Example(Enum):
    """Provide exmample schema object."""

    NAME = auto()
    TARGET = auto()


def test_select() -> None:
    """Test select statement."""
    statement = (
        SELECT()
        .FROM(Example)
        .WHERE(
            (Example.NAME | EQ | ':name')
            | AND
            | (Example.TARGET | EQ | ':target')
        )
        .END()
    )
    # cursor.execute(statement)
    assert statement == (
        'SELECT * FROM Example '
        + 'WHERE Example.NAME = :name '
        + 'AND Example.TARGET = :target;'
    )


def test_select_in() -> None:
    """Test select statement."""
    statement = (
        SELECT()
        .FROM(Example)
        .WHERE(Example.TARGET)
        .IN(':test1', ':test2')
        .END()
    )
    # cursor.execute(statement)
    assert statement == (
        'SELECT * FROM Example '
        + 'WHERE Example.TARGET '
        + 'IN (:test1, :test2);'
    )


def test_select_between() -> None:
    """Test select statement."""
    statement = (
        SELECT()
        .FROM(Example)
        .WHERE(Example.TARGET)
        .BETWEEN(':range1' | AND | ':range2')
        .END()
    )
    # cursor.execute(statement)
    assert statement == (
        'SELECT * FROM Example '
        + 'WHERE Example.TARGET '
        + 'BETWEEN :range1 AND :range2;'
    )
