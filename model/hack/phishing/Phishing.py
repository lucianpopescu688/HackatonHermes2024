# Phishing.py
from model.hack.virus.Virus import Virus
from model.hack.HackUpgrade.phishingUpgrade import PhishingUpgrade

class Phishing(Virus):
    def __init__(self, name: str, victims: int, price: float, risk: float, efficiency: float = 0.3, stealth: float = 0.1):
        super().__init__(name, victims, price, risk)
        self.efficiency = efficiency
        self.stealth = stealth
        self.upgrade_prices = {
            "efficiency": PhishingUpgrade(self, "efficiency").get_upgrade_prices("efficiency"),
            "stealth": PhishingUpgrade(self, "stealth").get_upgrade_prices("stealth")
        }

    def spread(self):
        print(f"{self.name} is spreading!")
        self.victims += int(self.victims * 0.5)  # Example spread rate
        self.risk += int(self.risk * 0.1)  # Increase risk

    def upgrade(self, upgrade_type: str, player):
        upgrade = PhishingUpgrade(self, player)
        upgrade.upgrade(upgrade_type)

    def reward(self):
        return self.victims * 0.5  # Example reward generator

    def execute(self):
        self.spread()
        computers_infected = self.victims  # Example value
        money_gained = computers_infected * self.efficiency  # Example value
        return [computers_infected, money_gained]

    def update_victims(self,victims):
        self.victims+=victims
        return self.victims
        pass
