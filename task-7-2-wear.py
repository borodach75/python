# Одежда


from abc import ABC, abstractmethod

class Wear(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def consum(self):
        pass

class Coat(Wear):
    def __init__(self, v):
        self.__v = v
        self.__consum = v / 6.5 + 0.5

    @property
    def consum(self):
        return self.__consum

class Suit(Wear):
    def __init__(self, h):
        self.__h = h

    @property
    def consum(self):
        self.__consum = 2 * self.__h + 0.3
        return self.__consum

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        self.__h = h


coat_1 = Coat(8)    # V=8
print(coat_1.consum)
suit_1 = Suit(2)    # H=2
print(suit_1.consum)
suit_1.h = 1        # H=1
print(suit_1.consum)
