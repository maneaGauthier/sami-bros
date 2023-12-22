from abc import ABC, abstractmethod

class BehaviorShoot(ABC):
    def __init__(self):
        self.__weapon = None
    @abstractmethod
    def shoot(self):
        ...
    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, weapon) -> None:
        self.__weapon = weapon
