"""Demonstrate basic SQL statement."""

from sql import ALTER_DATABASE

# from sql import AND, END, EQ, FROM, ALTER_DATABASE, WHERE


def test_alter_database() -> None:
    """Test alter statement."""
    statement = ALTER_DATABASE(':old_name').RENAME_TO(':new_name').END()
    assert statement == ('ALTER DATABASE :old_name RENAME TO :new_name;')
    # cursor.execute(statement)


# def test_alter_table() -> None:
#     """Test alter statement."""
#     statement = (
#         ALTER_TABLE()
#         .FROM(Example)
#         .WHERE(Example.TARGET)
#         .IN(':test1', ':test2')
#         .END()
#     )
#     # cursor.execute(statement)
#     assert statement == (
#         'ALTER TABLE * FROM Example '
#         + 'WHERE Example.TARGET '
#         + 'IN (:test1, :test2);'
#     )


# def test_alter_view() -> None:
#     """Test alter statement."""
#     statement = (
#         ALTER_VIEW()
#         .FROM(Example)
#         .WHERE(Example.TARGET)
#         .BETWEEN(':range1' | AND | ':range2')
#         .END()
#     )
#     # cursor.execute(statement)
#     assert statement == (
#         'ALTER VIEW * FROM Example '
#         + 'WHERE Example.TARGET '
#         + 'BETWEEN :range1 AND :range2;'
#     )
