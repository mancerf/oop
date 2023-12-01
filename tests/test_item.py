"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

@pytest.fixture
def shop_item():
    return Item('Тигель', 1800, 10)

def test_name_shop(shop_item):
    assert shop_item.name == 'Тигель'
    assert shop_item.name != 'book'

def test_price_shop(shop_item):
    assert shop_item.price == 1800
    assert shop_item.price != 1111

def test_quantity_shop(shop_item):
    assert shop_item.quantity == 10
    assert shop_item.quantity != 9

def test_total_price(shop_item):
    assert shop_item.calculate_total_price() == 1800*10

def test_low_price(shop_item):
     shop_item.apply_discount()
     assert shop_item.price == 1800*1