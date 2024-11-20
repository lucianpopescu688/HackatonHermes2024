# model/hack/attack/AttackOnCompany.py
import random
from enum import Enum

class CompanyNames(Enum):
    GOOGLE = "Google"
    MICROSOFT = "Microsoft"
    AMAZON = "Amazon"
    FACEBOOK = "Facebook"
    TESLA = "Tesla"
    CLOUDFLIGHT = "Cloudflight"

class AttackOnCompany:
    def __init__(self, reward, chance_of_success, risk, protection):
        self.__reward = reward
        self.__chance_of_success = chance_of_success
        self.__risk = risk
        self.__company_name = random.choice(list(CompanyNames))
        self.__protection = protection

    # Getters
    def get_reward(self):
        return self.__reward

    def get_chance(self):
        return self.__chance_of_success

    def get_risk(self):
        return self.__risk

    def get_company_name(self):
        return self.__company_name

    # Setters
    def set_reward(self, reward):
        self.__reward = reward

    def set_chance_of_success(self, chance):
        self.__chance_of_success = chance

    def set_risk(self, risk):
        self.__risk = risk

    # Method for the attack
    def attack_on_company(self, success_rate):
        if success_rate > random.randint(0, 100):
            return [self.get_reward(), self.get_risk()]
        else:
            return [0, self.get_risk()]