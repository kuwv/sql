"""Demonstrate basic SQL statement."""

from sql import EQ, DELETE

# from sql import AND, END, EQ, FROM, SELECT, WHERE


def test_select() -> None:
    """Test select statement."""
    statement = (
        DELETE().FROM('Example').WHERE('Example.NAME' | EQ | ':name').END()
    )
    # cursor.execute(statement)
    assert statement == ('DELETE FROM Example WHERE Example.NAME = :name;')
