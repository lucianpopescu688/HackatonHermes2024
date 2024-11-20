# BruteForce.py
from model.hack.hack import Hack
from model.hack.HackUpgrade.phishingUpgrade import BruteForceUpgrade

class BruteForce(Hack):
    def __init__(self, name: str, price: float, risk: float, attempts: int):
        super().__init__(price, name, risk)
        self.attempts = attempts
        self.success_rate = 0.1  # Base success rate
        self.active = False
        self.upgrade_prices = {
            "attempt_speed": 100.0
        }
        self.upgrade_manager = BruteForceUpgrade(self, self.upgrade_prices)


    def attack(self):
        print(f"{self.name} is attempting to brute force with {self.attempts} attempts!")
        self.attempts += int(self.attempts * 0.1)  # Increase attempts

    def upgrade(self, upgrade_type: str,player):
        upgrade = BruteForceUpgrade(self,player)
        upgrade.upgrade(upgrade_type)

    def reward(self):
        return self.attempts * 0.3  # Example reward generator

    def execute(self):
        self.attack()
        print(f"Executing {self.name} with {self.attempts} attempts and success rate {self.success_rate:.2f}")
        return [self.reward(), self.risk]

    def update_victims(self, count: int):
        self.attempts += count