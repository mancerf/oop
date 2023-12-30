from src.item import Item


class Phone(Item):
    """
    Дочерний класс от класса Item, представляющий телефоны
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляка класса
        :param name: имя
        :param price: цена за штуку
        :param quantity: количество телефонов
        :param number_of_sim: количество сим-карт

        взятие инициализации у родительского класса Item
        проверка количества сим-карт
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Геттер количества сим-карт
        :return:
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim):
        if sim <= 0:
            print('ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = sim
