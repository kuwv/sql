"""Provide a example database model."""

# from sql.dsl import EQ, END, INSERT_INTO, VALUES
from sql import INSERT_INTO


def test_insert() -> None:
    """Test insert statement."""
    statement = INSERT_INTO('example.name').VALUES(':name').END()
    assert statement == 'INSERT INTO example.name VALUES (:name);'

    statement = (
        INSERT_INTO('example', ('id', 'name')).VALUES(':id', ':name').END()
    )
    assert statement == ('INSERT INTO example (id, name) VALUES (:id, :name);')


# def test_insert_multiple_rows() -> None:
#     """Test insertion of multiple rows."""
#     statement = INSERT_INTO(
#         'Customers',
#         (
#             'CustomerName',
#             'ContactName',
#             'Address',
#             'City',
#             'PostalCode',
#             'Country',
#         ),
#     ).VALUES(
#         (
#             ':customer_name0',
#             ':contact_name0',
#             ':address0',
#             ':city0',
#             ':postal_cide0',
#             ':country0',
#         ),
#         (
#             ':customer_name1',
#             ':contact_name1',
#             ':address1',
#             ':city1',
#             ':postal_code1',
#             ':country1',
#         ),
#         (
#             ':customer_name2',
#             ':contact_name2',
#             ':address2',
#             ':city2',
#             ':postal_code2',
#             ':country2',
#         ),
#     )
#     print(statement)
#     # assert statement == (
#     #     'INSERT INTO Customers ('
#     #     +   'CustomerName, ContactName, Address, City, PostalCode, Country'
#     #     + ') '
#     #     +   'VALUES '
#     #     + '('
#     #     +   ':customer_name0, '
#     #     +   ':contact_name0, '
#     #     +   ':address0, '
#     #     +   ':city0, '
#     #     +   ':postal_cide0, '
#     #     +   ':country0'
#     #     + '), '
#     #     + '('
#     #     +   ':customer_name1, '
#     #     +   ':contact_name1, '
#     #     +   ':address1, '
#     #     +   ':city1, '
#     #     +   ':postal_code1, '
#     #     +   ':country1'
#     #     + '), '
#     #     + '('
#     #     +   ':customer_name2, '
#     #     +   ':contact_name2, '
#     #     +   ':address2, '
#     #     +   ':city2, '
#     #     +   ':postal_code2, '
#     #     +   ':country2'
#     #     + ');'


def test_insert_select() -> None:
    """Test insert statement where match exists."""
    statement = (
        INSERT_INTO('Customers', ('Name', 'City', 'Country'))
        .SELECT('Name', 'City', 'Country')
        .FROM('Suppliers')
        .END()
    )
    assert statement == (
        'INSERT INTO Customers (Name, City, Country) '
        + 'SELECT Name, City, Country '
        + 'FROM Suppliers;'
    )
