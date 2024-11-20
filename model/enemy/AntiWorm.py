import random


class AntiWorm:
    def __init__(self):
        # Atribute private
        self.__public_awareness = 0  # Gradul de conștientizare publică
        self.__efficiency = 0.5  # Eficiența actuală a virusului
        self.__inactive_time = 0  # Timpul de inactivitate (setat din exterior)
        self.__active_time = 0  # Timpul de activitate (setat din exterior)
        self.__count = 0  # Numărul de utilizări (setat din exterior)
        self.__computers_infected = 0  # Numărul de computere infectate (setat din exterior)
        self.__previous_count = 0

    # Getters
    def get_public_awareness(self):
        return self.__public_awareness

    def get_efficiency(self):
        return self.__efficiency

    def get_inactive_time(self):
        return self.__inactive_time

    def get_active_time(self):
        return self.__active_time

    def get_count(self):
        return self.__count

    def get_previous_count(self):
        return self.__previous_count

    def get_computers_infected(self):
        return self.__computers_infected

    # Setters
    def set_inactive_time(self, time):
        self.__inactive_time = time

    def set_active_time(self, time):
        self.__active_time = time

    def set_count(self, count):
        self.__previous_count = self.__count
        self.__count = count

    def set_computers_infected(self, infected):
        self.__computers_infected = infected

    def set_public_awareness(self, awareness):
        self.__public_awareness = awareness

    def set_efficiency(self, efficiency):
        self.__efficiency = efficiency

    def update_after_computers_infected_and_activity(self, computersInfected, activeTime):
        if (computersInfected > 10 and activeTime > 60) or computersInfected > 150 or activeTime > 200 :
            self.set_public_awareness(self.get_public_awareness() * 1.25)
            self.set_efficiency(self.get_efficiency() * 1.10)

    def update_after_inactivity(self, inactiveTime):
        if inactiveTime > 100:
            self.set_efficiency(self.get_efficiency() * 0.95)
            self.set_public_awareness(self.get_public_awareness() * 0.70)

    def update_after_count(self, count):
        if count > self.__previous_count:
            if random.uniform(0, 100) > 50:
                self.set_efficiency(self.get_efficiency() *
                random.uniform(1, 1.5))

    def check_and_default_money(self, activeTime):
        chance = min(activeTime / 1000000, 1)  # Cap the chance at 1 (100%)
        if random.uniform(0, 1) < chance:
            return True
        return False



                # Reprezentare textuală a stării obiectului
    def __str__(self):
        return (f"AntiWorm State:\n"
                f"  Public Awareness: {self.__public_awareness:.2f}\n"
                f"  Efficiency: {self.__efficiency:.2f}\n"
                f"  Inactive Time: {self.__inactive_time}\n"
                f"  Active Time: {self.__active_time}\n"
                f"  Count: {self.__count}\n"
                f"  Computers Infected: {self.__computers_infected}\n")