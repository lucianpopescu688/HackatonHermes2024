# phishingUpgrade.py
class PhishingUpgrade:
    upgrade_prices = {
        "efficiency": 300.0,
        "stealth": 200.0
    }

    def __init__(self, target, player):
        self.target = target
        self.player = player

    def upgrade(self, attribute):
        if attribute in self.upgrade_prices:
            price = self.upgrade_prices[attribute]
            if self.player.money >= price:
                if hasattr(self.target, attribute):
                    current_value = getattr(self.target, attribute)
                    if isinstance(current_value, (int, float)):
                        setattr(self.target, attribute, current_value * 1.1)  # Increase by 10%
                        self.player.money -= price  # Deduct the price from player's money
                        self.upgrade_prices[attribute] *= 1.2  # Increase the price for the next upgrade
                        print(f"{attribute} upgraded to {getattr(self.target, attribute)} for ${price}")
                    else:
                        print(f"Cannot upgrade {attribute}, not a numeric value")
                else:
                    print(f"{self.target} has no attribute {attribute}")
            else:
                print("Not enough money to upgrade")
        else:
            print("Invalid upgrade type")

    def get_upgrade_prices(self, upgrade_type):
        return self.upgrade_prices.get(upgrade_type, None)

class BruteForceUpgrade:
    upgrade_prices = {
        "attempt_speed": 100.0,
    }

    def __init__(self, target, player):
        self.target = target
        self.player = player

    def upgrade(self, attribute):
        if attribute in self.upgrade_prices:
            price = self.upgrade_prices[attribute]
            if self.player.money >= price:
                if hasattr(self.target, attribute):
                    current_value = getattr(self.target, attribute)
                    if isinstance(current_value, (int, float)):
                        setattr(self.target, attribute, current_value * 55)
        else:
            print("Invalid upgrade type")

    def get_upgrade_prices(self):
        return self.upgrade_prices
