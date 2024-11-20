import random
from enum import Enum

# Enum pentru numele guvernelor
class GovernmentNames(Enum):
    USA = "USA"
    CHINA = "China"
    RUSSIA = "Russia"
    GERMANY = "Germany"
    UK = "UK"
    INDIA = "India"
    AZERBAIJAN = "Azerbaijan"
    QATAR = "Qatar"
    TADJIKISTAN = "Tadjikistan"


# Clasa pentru atacuri asupra guvernelor
class GovernmentClass:
    def __init__(self, reward, chance_of_success, risk, protection):
        self.__reward = reward  # Recompensa pentru atac
        self.__chance_of_success = chance_of_success  # Șansa de succes 1-100
        self.__risk = risk  # Risc asociat atacului
        self.__government_name = random.choice(list(GovernmentNames)).value  # Alegerea aleatorie a unui guvern
        self.__protection = protection  # Nivelul de protecție al guvernului

    # Getters
    def get_reward(self):
        return self.__reward

    def get_chance(self):
        return self.__chance_of_success

    def get_risk(self):
        return self.__risk

    def get_government_name(self):
        return self.__government_name

    # Setters
    def set_reward(self, reward):
        self.__reward = reward

    def set_chance_of_success(self, chance):
        self.__chance_of_success = chance

    def set_risk(self, risk):
        self.__risk = risk

    def set_protection(self, protection):
        self.__protection = protection

    # Metoda pentru atacul asupra unui guvern
    def attack_on_government(self, success_rate):
        # Compară succesul aleatoriu cu succesul dat de utilizator
        if success_rate > random.randint(0, 100):
            return [self.get_reward(), self.get_risk()]  # Atacul a reușit
        else:
            return [0, self.get_risk()]  # Atacul a eșuat
