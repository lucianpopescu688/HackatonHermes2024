# Controller/Controller.py
import time

from model.Player import Player
from model.hack.attack.AttackOnCompany import AttackOnCompany
from model.hack.bruteForce.BruteForce import BruteForce
from model.hack.virus.Worm import Worm
from model.hack.virus.Ransomware import Ransomware
from model.hack.phishing.Phishing import Phishing
from model.exceptions.GameException import GameException
from model.enemy.AntiWorm import AntiWorm

import random

class Controller:
    def __init__(self, player_name):
        self.brute_force_upgrades = 0
        self.p = Player(player_name)
        self.worm = Worm("Worm Virus", 1, 200, 2.5, 2, 1)
        self.ransomware = Ransomware("Ransomware Virus", 0, 500, 5, 10, 100)
        self.phishing = Phishing("Phishing Scams", 0, 50, 1)
        self.brute_force = BruteForce("Brute Force", 0, 100, 1)
        self.antiworm = AntiWorm()
        self.worm_upgrades = 0
        self.ransomware_upgrades = 0  # Add ransomware upgrade counter
        self.phishing_upgrades = 0  # Add phishing upgrade counter
        self.boughtWorm = False
        self.boughtRansom = False
        self.boughtPhis = False
        self.boughtBrute = False
        self.worm_automation_enabled = False
        self.brute_force_automation_enabled = False
        self.ransom_automation_enabled = False
        self.phishing_automation_enabled = False
        self.companies_hacked = 0
        self.company_chance_of_success = 0.5
        self.attack_on_company = self.initialize_attack_on_company()
        self.government_chance_of_success = 0.1
        self.attack_on_government = self.initialize_attack_on_government()

    def getActivePhishing(self):
        return self.phishing_automation_enabled

    def getActiveWorm(self):
        return self.worm_automation_enabled

    def getActiveRansomware(self):
        return self.ransom_automation_enabled

    def getActiveBruteForce(self):
        return self.brute_force_automation_enabled

    def upgradeBruteForceAttempts(self):
        if self.p.money >= self.brute_force.upgrade_prices["attempt_speed"]:
            self.brute_force.upgrade("attempt_speed", self.p)
            self.brute_force_upgrades += 1

    def performBruteForce(self):
        if not self.boughtBrute:
            raise GameException("You do not have this yet")
        else:
            if self.brute_force.active:
                result = self.brute_force.execute()
                self.p.add_computers(result[0])
                self.p.add_money(result[1])

    def getName(self):
        return self.p.name

    def getInfectedCount(self):
        return self.p.computers_infected

    def getMoney(self):
        return self.p.money

    def get_hack_chance_company(self):
        cost = 5000  # Define the cost for checking hack chance
        if self.p.money >= cost:
            self.p.money -= cost
            cost*=10
            self.company_chance_of_success=min(80, self.attack_on_company.get_chance() + 0.08 * self.get_all_upgrades())
            return min(80, self.attack_on_company.get_chance() + 0.08 * self.get_all_upgrades())
        else:
            print("Not enough money to check hack chance for company")
            return 0

    def get_hack_chance_government(self):
        cost = 100000  # Define the cost for checking hack chance
        if self.p.money >= cost:
            self.p.money -= cost
            cost*=10
            self.government_chance_of_success=min(40, self.attack_on_government.get_chance() + 0.01 * self.get_all_upgrades())
            return min(40, self.attack_on_government.get_chance() + 0.01 * self.get_all_upgrades())
        else:
            print("Not enough money to check hack chance for government")
            return 0
    def initialize_attack_on_company(self):
        reward=100
        risk=50
        protection=0.5
        return AttackOnCompany(reward, self.company_chance_of_success, risk, protection)

    def perform_attack_on_company(self):
        success_rate = self.attack_on_company.get_chance() + 0.01 * self.get_all_upgrades()
        result = self.attack_on_company.attack_on_company(success_rate)
        self.p.add_money(result[0])
        print(f"Attack on {self.attack_on_company.get_company_name().value} {'succeeded' if result[0] > 0 else 'failed'} with reward {result[0]} and risk {result[1]}")

    def toggle_worm_automation(self):
        self.worm_automation_enabled = not self.worm_automation_enabled

    def toggle_ransom_automation(self):
        self.ransom_automation_enabled = not self.ransom_automation_enabled

    def toggle_phishing_automation(self):
        self.phishing_automation_enabled = not self.phishing_automation_enabled

    def toggle_brute_force_automation(self):
        self.brute_force_automation_enabled = not self.brute_force_automation_enabled

    def is_worm_automation_enabled(self):
        return self.worm_automation_enabled

    def is_ransom_automation_enabled(self):
        return self.ransom_automation_enabled

    def is_phishing_automation_enabled(self):
        return self.phishing_automation_enabled

    def upgradeWormSpeed(self):
        if self.p.money >= self.worm.upgrade_prices["speed"]:
            self.worm.upgrade("speed", self.p)
            self.worm_upgrades += 1

    def upgradeWormStealth(self):
        if self.p.money >= self.worm.upgrade_prices["stealth"]:
            self.worm.upgrade("stealth", self.p)
            self.worm_upgrades += 1

    def performWorm(self):
        if not self.boughtWorm:
            raise GameException("You do not have this yet")
        else:
            if self.worm.active:
                result = self.worm.execute()
                self.p.add_computers(result[0])
                self.p.add_money(result[1])
                self.activate_countermeasures()

    def upgradeRansomwareEncryption(self):
        if self.p.money >= self.ransomware.upgrade_prices["encryption_strength"]:
            self.ransomware.upgrade("encryption_strength", self.p)
            self.ransomware_upgrades += 1

    def upgradeRansomwareRansom(self):
        if self.p.money >= self.ransomware.upgrade_prices["ransom_amount"]:
            self.ransomware.upgrade("ransom_amount", self.p)
            self.ransomware_upgrades += 1

    def performRansom(self):
        if not self.boughtRansom:
            raise GameException("You do not have this yet")
        else:
            if self.ransomware.active:
                result = self.ransomware.execute()
                self.p.add_computers(result[0])
                self.p.add_money(result[1])
                self.activate_ransomware_countermeasures()

    def upgradePhishingEfficiency(self):
        if self.p.money >= self.phishing.upgrade_prices["efficiency"]:
            self.phishing.upgrade("efficiency", self.p)
            self.phishing_upgrades += 1

    def upgradePhishingStealth(self):
        if self.p.money >= self.phishing.upgrade_prices["stealth"]:
            self.phishing.upgrade("stealth", self.p)
            self.phishing_upgrades += 1

    def performPhish(self):
        if not self.boughtPhis:
            raise GameException("you don't own this yet")
        else:
            result = self.phishing.execute()
            self.p.add_computers(result[0])
            self.p.add_money(result[1])
            self.activate_phishing_countermeasures()

    def activateWorm(self):
        self.worm.active = True
        self.boughtWorm = True
        self.worm.update_victims(1)

    def activateRansomware(self):
        self.ransomware.active = True
        self.boughtRansom = True
        self.ransomware.update_victims(1)

    def activatePhishing(self):
        self.phishing.active = True
        self.boughtPhis = True
        self.phishing.update_victims(1)

    def activateBruteForce(self):
        self.brute_force.active = not self.brute_force.active
        self.boughtBrute = True
        self.brute_force.update_victims(1)

    def activate_countermeasures(self):
        self.antiworm.update_after_computers_infected_and_activity(self.worm.computers_infected, self.worm.active_time)
        self.antiworm.update_after_inactivity(self.worm.inactive_time)
        self.antiworm.update_after_count(self.worm.count)
        if self.antiworm.check_and_default_money(self.worm.active_time):
            self.p.money /= 10
            print("money was lost due to penalty!")

    def activate_ransomware_countermeasures(self):
        if random.uniform(0, 1) < 0.1:  # 10% chance to trigger
            self.p.money /= 10
            print("money was lost due to ransomware penalty!")

    def activate_phishing_countermeasures(self):
        if random.uniform(0, 1) < 0.1:  # 10% chance to trigger
            self.p.money /= 10
            print("money was lost due to phishing penalty!")

    def display_antiworm_state(self):
        print(self.antiworm)

    def get_all_upgrades(self):
        return self.worm_upgrades+self.ransomware_upgrades+self.phishing_upgrades

    def start_company_hack(self):
        success_rate = self.get_hack_chance_company()
        result = self.attack_on_company.attack_on_company(success_rate)
        if result[0] > 0:
            self.companies_hacked += 1
            self.attack_on_company = self.initialize_attack_on_company()
        self.p.add_money(result[0])
        print(f"Attack on {self.attack_on_company.get_company_name().value} {'succeeded' if result[0] > 0 else 'failed'} with reward {result[0]} and risk {result[1]}")
        return self.attack_on_company.get_company_name().value

    def start_government_hack(self):
        success_rate = self.get_hack_chance_government()
        result = self.attack_on_government.attack_on_company(success_rate)
        if result[0] > 0:
            self.attack_on_government = self.initialize_attack_on_government()
        self.p.add_money(result[0])
        print(
            f"Attack on government {'succeeded' if result[0] > 0 else 'failed'} with reward {result[0]} and risk {result[1]}")
        return result[0] > 0

    def initialize_attack_on_government(self):
        reward=1000000
        risk=90
        protection=0.9
        return AttackOnCompany(reward, self.government_chance_of_success, risk, protection)
