# Virus.py
from model.hack.hack import Hack

class Virus(Hack):
    def __init__(self, name: str, victims: int, price: float, risk: float):
        super().__init__(price, name, risk)
        self.victims = victims
        self.efficiency = 1.0  # Base efficiency


    def spread(self):
        print(f"{self.name} is spreading!")
        self.victims += int(self.victims * 0.1)  # Example spread rate

    def upgrade(self, upgrade_type: str):
        if upgrade_type == "speed":
            self.efficiency += 0.2
        elif upgrade_type == "stealth":
            self.efficiency += 0.1
        else:
            print("Invalid upgrade type!")

    def reward(self):
        return self.victims * 0.1  # Example reward generator

    def __str__(self):
        return f"Virus Name: {self.name}, Victims/Day: {self.victims}, Efficiency: {self.efficiency:.2f}"