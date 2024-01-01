from src.item import Item


class Lang:
    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"





class Keyboard(Item, Lang):
    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price,quantity)
        Lang.__init__(self)
