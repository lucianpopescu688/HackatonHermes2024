from abc import ABC, abstractmethod


class MinigameInterface(ABC):
    def __init__(self, name:str, reward:int):
        self.matrix =  [[0 for _ in range(4)] for _ in range(4)]
        self._name = name
        self._reward = reward

    def getName(self):
        return self._name

    def getReward(self):
        return self._reward

    @abstractmethod
    def evolveReward(self):
        pass

    @abstractmethod
    def complete(self):
        pass
