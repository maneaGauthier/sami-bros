from behaviorshootlikepistol import BehaviorShootLikePistol
from weapon import Weapon
from ursina import *

class NailerGun(Weapon):
    def __init__(self):
        super().__init__(BehaviorShootLikePistol(), model='assets/3D/silent_nail_gun.glb',
                         rotation=(0,90,0),
                         position=(1,-0.2,1), scale=0.05, texture='assets/textures/Body_baseColor.png')

    def update(self):
        if held_keys['left mouse']:
            self.shoot()