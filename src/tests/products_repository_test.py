import pytest
from src.models.sqlite.settings.connection import SqliteConnectionHandler
from src.models.sqlite.repository.products_repository import ProductsRepository

conn_handler = SqliteConnectionHandler()
conn = conn_handler.connect()

@pytest.mark.skip(reason='Interacao com o banco de dados')
def test_insert_products():
    repo = ProductsRepository(conn)

    name = 'Test Product 2'
    price = 10.0
    quantity = 8

    repo.insert_product(name, price, quantity)

@pytest.mark.skip(reason='Interacao com o banco de dados')
def test_find_product_by_name():
    repo = ProductsRepository(conn)

    name = 'Test Product 2'

    product = repo.find_product_by_name(name)

    print(product)
    print(type(product))

    assert product[1] == name
