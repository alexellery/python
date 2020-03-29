from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def fabric_usage(self):
        pass

    @abstractmethod
    def total_usage(a, b):
        return a + b


class Coat(Clothes):
    def __init__(self, name, size):
        self.__size = size
        super().__init__(name)

    @property
    def fabric_usage(self):
        return self.__size * 6.5 + 0.5

    @staticmethod
    def total_usage(a, b):
        return a + b


class Costume(Clothes):

    def __init__(self, name, height):
        self.__height = height
        super().__init__(name)

    @property
    def fabric_usage(self):
        return self.__height * 2 + 0.3

    @staticmethod
    def total_usage(a, b):
        return a + b


armani = Coat('Venus', 5)
versace = Costume('Mercury', 180)

print(f'Всего будет потрачено ткани: {versace.total_usage(armani.fabric_usage, versace.fabric_usage)}')


