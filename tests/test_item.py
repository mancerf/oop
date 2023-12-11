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

def test_lenght_name(shop_item):
    shop_item.name = 'СуперСмартфон'
    assert len(shop_item.name) == 10

def test_Item_string_to_number(shop_item):
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_instantiate_from_csv(shop_item):
    Item.instantiate_from_csv(r'C:\Users\Все пользователи\electronics-shop-project\src\items.csv')
    assert len(Item.all) == 5