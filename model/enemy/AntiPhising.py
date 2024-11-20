
import random

class AntiPhising:
    def __init__(self):
        self.__public_awareness = 0
        self.__inactive_time = 0
        self.__active_time = 0
        self.__computers_infected = 0

    def get_public_awareness(self):
        return self.__public_awareness

    def get_inactive_time(self):
        return self.__inactive_time

    def get_active_time(self):
        return self.__active_time

    def get_computers_infected(self):
        return self.__computers_infected

    def set_inactive_time(self, time):
        self.__inactive_time = time

    def set_active_time(self, time):
        self.__active_time = time

    def set_public_awareness(self, awareness):
        self.__public_awareness = awareness

    def set_computers_infected(self, computers_infected):
        self.__computers_infected = computers_infected

    def update_after_computers_infected_and_activity(self, computersInfected, activeTime):
        if (computersInfected > 10 and activeTime > 60) or computersInfected > 150 or activeTime > 200:
            self.set_public_awareness(self.get_public_awareness() * 1.25)

    def update_after_inactivity(self, inactiveTime):
        if inactiveTime > 100:
            self.set_public_awareness(self.get_public_awareness() * 0.70)

    def update_active_time(self, time):
        self.__active_time += time

    def update_inactive_time(self, time):
        self.__inactive_time += time

    def check_and_fire_event(self):
        if random.random() < 0.1:  # 10% chance to fire
            self.cause_extremely_bad_consequences()

    def cause_extremely_bad_consequences(self):
        print("Extremely bad consequences have occurred!")
        self.set_public_awareness(0)
        self.set_computers_infected(0)

    def __str__(self):
        return (f"AntiPhising State:\n"
                f"  Public Awareness: {self.__public_awareness:.2f}\n"
                f"  Inactive Time: {self.__inactive_time}\n"
                f"  Active Time: {self.__active_time}\n"
                f"  Computers Infected: {self.__computers_infected}\n")