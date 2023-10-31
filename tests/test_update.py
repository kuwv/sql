"""Demonstrate basic SQL statement."""
from enum import Enum, auto

from sql import AND, EQ, UPDATE

# from sql import AND, END, EQ, SET, UPDATE, WHERE


class Example(Enum):
    """Provide exmample schema object."""

    NAME = auto()
    TARGET = auto()


def test_update() -> None:
    """Test update statement."""
    statement = (
        UPDATE(Example)
        .SET(Example.TARGET | EQ | ':target_update')
        .WHERE(
            (Example.NAME | EQ | ':name')
            | AND
            | (Example.TARGET | EQ | ':target')
        )
        .END()
    )
    # cursor.execute(statement)
    assert statement == (
        'UPDATE Example '
        + 'SET Example.TARGET = :target_update '
        + 'WHERE Example.NAME = :name '
        + 'AND Example.TARGET = :target;'
    )
