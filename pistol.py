from behaviorshootlikepistol import BehaviorShootLikePistol
from player import Player
from weapon import Weapon
from ursina import *

class Pistol(Weapon):
    def __init__(self):
        super().__init__(BehaviorShootLikePistol(), model='assets/3D/Beretta Pistol.fbx',
                         position=(2,0.7,2), scale=0.001, texture='Berreta M9_Material_BaseColor')

    def update(self):
        if held_keys['left mouse']:
            self.shoot()








