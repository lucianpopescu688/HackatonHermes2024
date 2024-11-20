
from model.exceptions.GameException import GameException
from model.hack.hack import Hack
from model.hack.virus.Virus import Virus

class Player:
    def __init__(self, name: str):
        self.name = name
        self.computers_infected = 0
        self.money = 300.0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        if value < 0:
            raise ValueError("Money cannot be negative")
        self._money = value

    def add_money(self, amount: float):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.money += amount

    def subtract_money(self, amount: float):
        if amount > self.money:
            raise GameException("You're poor :(")
        self.money -= amount

    def add_computers(self, number: int):
        self.computers_infected += number

    def subtract_computers(self, number: int):
        self.computers_infected = max(0, self.computers_infected - number)