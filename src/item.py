import csv
from src.csv_err import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __str__(self):
        return self.__name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[0:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    def __add__(self, other):
        """
        Сложение количества товаров из классов Item и Phone
        (сложение по количеству товара в магазине)
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError()

    @classmethod
    def instantiate_from_csv(cls, doc):
        '''класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv'''
        with open(doc, 'r', encoding='cp1251') as file:
            if file == None:
                raise FileNotFoundError('Отсутствует файл item.csv')
            else:
                reader = csv.DictReader(file)
                Item.all.clear()
                for row in reader:
                    if not row['name']:
                        raise InstantiateCSVError("Файл item.csv поврежден отсутвует название ")
                    if not row['price']:
                        raise InstantiateCSVError("Файл item.csv поврежден отсутсвует цена")
                    if not row['quantity']:
                        raise InstantiateCSVError("Файл item.csv поврежден отсутсвует колличесвто ")
                    cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(value):
        """статический метод, возвращающий число из числа-строки"""
        if '.' in value:
            value = float(value)
            return int(value)
        return int(value)
