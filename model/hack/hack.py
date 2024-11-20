from abc import ABC, abstractmethod

class Hack(ABC):
    def __init__(self, price, name,risk):
        self._price = price
        self._name = name
        self._risk = risk
        self.active = True

    def activate(self):
        self._active = True

    def deactivate(self):
        self.active = False

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def risk(self):
        return self._risk

    @risk.setter
    def risk(self, risk):
        self._risk=risk

    @abstractmethod
    def execute(self):
        pass
