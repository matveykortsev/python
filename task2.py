from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, params):
        self.params = params

    @abstractmethod
    def calculate(self):
        pass


class Suit(Cloth):

    @property
    def calculate(self):
        return self.params / 6.5 + 0.5


class Coat(Cloth):

    @property
    def calculate(self):
        return 2 * self.params + 0.3


coat = Coat(30)
suit = Suit(40)
print(coat.calculate)
print(suit.calculate)