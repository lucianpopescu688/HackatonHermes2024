# Ransomware.py
from model.hack.virus.Virus import Virus
from model.hack.HackUpgrade.HackUpgrade import HackUpgradeRansomware

class Ransomware(Virus):
    def __init__(self, name: str, victims: int, price: float, risk: float, encryption_strength: float = 1.0, ransom_amount: float = 1000.0):
        super().__init__(name, victims, price, risk)
        self.encryption_strength = encryption_strength
        self.ransom_amount = ransom_amount
        self.upgrade_prices = {
            "encryption_strength": HackUpgradeRansomware(self, "encryption_strength").get_upgrade_prices("encryption_strength"),
            "ransom_amount": HackUpgradeRansomware(self, "ransom_amount").get_upgrade_prices("ransom_amount")
        }

    def spread(self):
        print(f"{self.name} is spreading!")
        self.victims += int(self.victims * 1.1)  # Example spread rate

    def upgrade(self, upgrade_type: str, player):
        upgrade = HackUpgradeRansomware(self, player)
        upgrade.upgrade(upgrade_type)

    def reward(self):
        return self.victims * self.ransom_amount * 0.1  # Example reward generator

    def execute(self):
        self.spread()
        computers_infected = self.victims  # Example value
        money_gained = computers_infected * self.ransom_amount * self.encryption_strength * 0.1  # Factor in encryption_strength
        return [computers_infected, money_gained]

    def update_victims(self,victims):
        self.victims+=victims
        return self.victims
        pass