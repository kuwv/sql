"""Demonstrate basic SQL statement."""

from sql import GT, SELECT

# from sql import AND, END, EQ, FROM, SELECT, WHERE


def test_group_by() -> None:
    """Test select statement."""
    statement = SELECT().FROM('Person').GROUP_BY('state').END()
    # cursor.execute(statement)
    assert statement == ('SELECT * FROM Person GROUP BY state;')


def test_group_by_having() -> None:
    """Test select statement."""
    statement = (
        SELECT()
        .FROM('Person')
        .GROUP_BY('state')
        .HAVING('age' | GT | ':age')
        .END()
    )
    # cursor.execute(statement)
    assert statement == (
        'SELECT * FROM Person GROUP BY state HAVING age > :age;'
    )


def test_order_by() -> None:
    """Test select statement."""
    statement = SELECT().FROM('Person').ORDER_BY('name').END()
    # cursor.execute(statement)
    assert statement == ('SELECT * FROM Person ORDER BY name;')


def test_order_by_asc() -> None:
    """Test select statement."""
    statement = SELECT().FROM('Person').ORDER_BY('name').ASC().END()
    # cursor.execute(statement)
    assert statement == ('SELECT * FROM Person ORDER BY name ASC;')


def test_order_by_desc() -> None:
    """Test select statement."""
    statement = SELECT().FROM('Person').ORDER_BY('name').DESC().END()
    # cursor.execute(statement)
    assert statement == ('SELECT * FROM Person ORDER BY name DESC;')
