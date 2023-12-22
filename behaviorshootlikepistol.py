from behaviorshoot import BehaviorShoot
from ursina import *

class BehaviorShootLikePistol(BehaviorShoot):

    def __init__(self):
        super().__init__()


    def shoot(self):
        if not self.weapon.on_cooldown:
            self.weapon.on_cooldown = True
            #self.weapon.behaviorshoot.muzzleflash.enabled = True
            from ursina.prefabs.ursfx import ursfx
            ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)], volume=0.5, wave='noise',
                  pitch=random.uniform(-13, -12), pitch_change=-12, speed=3.0)
            #invoke(self.weapon.behaviorshoot.muzzleflash.disable, delay=.05)
            invoke(setattr, self.weapon, 'on_cooldown', False, delay=.5)
            if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'hp'):
                mouse.hovered_entity.hp -= 20
                mouse.hovered_entity.blink(color.red)
