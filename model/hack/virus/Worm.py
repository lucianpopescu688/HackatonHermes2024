from bdb import effective
from model.hack.virus.Virus import Virus
from model.hack.HackUpgrade.HackUpgrade import HackUpgradeWorm as HackUpgrade, HackUpgradeWorm


class Worm:
    def __init__(self, name, computers_infected, damage, speed, stealth, count):
        self.name = name
        self.computers_infected = computers_infected
        self.damage = damage
        self.speed = speed
        self.stealth = stealth
        self.count = count
        self.active = False
        self.active_time = 0
        self.inactive_time = 0
        self.victims = 0
        self.spread_rate = 0.1
        self._risk = 0.05
        self.effectiveness = 1.0
        self.upgrade_count=0
        self.upgrade_prices ={
            "speed": HackUpgradeWorm(self, "speed").get_upgrade_prices("speed"),
            "stealth": HackUpgradeWorm(self, "stealth").get_upgrade_prices("stealth")
        }

    def spread(self):
        print(f"{self.name} is spreading!")
        self.victims += int(self.victims * self.spread_rate + 1)
        self._risk += int(self.getRisk() * 0.001)

    def upgrade(self, upgrade_type: str, player):
        upgrade = HackUpgrade(self, player)
        upgrade.upgrade(upgrade_type)
        self.upgrade_count += 1

    def getRisk(self):
        return self._risk

    def reward(self):
        return self.victims + self.victims * 0.2

    def execute(self):
        self.spread()
        self.active_time+=1
        computers_infected = int(self.victims)
        money_gained = computers_infected * self.effectiveness
        return [computers_infected, money_gained]

    def update_victims(self, victims):
        self.victims += victims
        return self.victims