# HackUpgrade.py
class HackUpgradeWorm:
    upgrade_prices = {
        "speed": 100.0,
        "stealth": 150.0
    }

    def __init__(self, target, player):
        self.target = target
        self.player = player

    def upgrade(self, attribute):
        if attribute in self.upgrade_prices:
            price = self.upgrade_prices[attribute]
            if self.player.money >= price:
                if attribute == "speed":
                    self.target.spread_rate *= 1.1  # Increase spread rate by 10%
                elif hasattr(self.target, attribute):
                    current_value = getattr(self.target, attribute)
                    if isinstance(current_value, (int, float)):
                        setattr(self.target, attribute, current_value * 8.9)  # Increase by 10%
                    else:
                        print(f"Cannot upgrade {attribute}, not a numeric value")
                else:
                    print(f"{self.target} has no attribute {attribute}")
                self.player.money -= price  # Deduct the price from player's money
                self.upgrade_prices[attribute] *= 1.2  # Increase the price for the next upgrade
                print(f"{attribute} upgraded for ${price}")
            else:
                print("Not enough money to upgrade")
        else:
            print("Invalid upgrade type")

    def get_upgrade_prices(self, upgrade_type):
        return self.upgrade_prices.get(upgrade_type, None)
# HackUpgrade.py

class HackUpgradeRansomware:
    upgrade_prices = {
        "encryption_strength": 500.0,
        "ransom_amount": 1000.0
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
                        setattr(self.target, attribute, current_value * 1.05)  # Increase by 5%
                        self.player.money -= price  # Deduct the price from player's money
                        self.upgrade_prices[attribute] *= 1.5  # Increase the price exponentially for the next upgrade
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