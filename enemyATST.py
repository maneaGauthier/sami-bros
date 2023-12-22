from ursina import *

from enemy import Enemy
from player import Player


class EnemyATST(Enemy):
    def __init__(self, player:Player,position, **kwargs):
        super().__init__(
            player=player,
            model='assets/3D/ATST.obj', scale=0.5,
            position=position,
            texture='assets/textures/ATST.png', texture_scale=0.5,
            **kwargs)


