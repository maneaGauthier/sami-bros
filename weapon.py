from ursina import *

from behaviorshoot import BehaviorShoot
from player import Player


class Weapon(Entity):
    __behaviorshoot: BehaviorShoot

    def __init__(self, behaviorshoot: BehaviorShoot,model ,position ,scale,texture ,rotation):
        super().__init__(self,
        parent=camera,
        model = model,
        position=position,
        scale = scale,
        texture= texture,
        rotation=rotation,
        on_cooldown = False,
        colider = 'mesh')

        self.__behaviorshoot = behaviorshoot
        behaviorshoot.weapon = self

    def shoot(self):
        self.__behaviorshoot.shoot()

    @property
    def behaviorshoot(self):
        return self.__behaviorshoot

    @behaviorshoot.setter
    def behaviorshoot(self, behaviorshoot: BehaviorShoot):
        self.__behaviorshoot = behaviorshoot
