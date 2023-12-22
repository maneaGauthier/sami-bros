from enemy import Enemy
from player import Player

class BossEnemy(Enemy):
    def __init__(self, player:Player, **kwargs):
        super().__init__(
            player=player,
            model='assets/3D/Kamdo.obj', scale=3,
            position=(114, 23, 82),
            texture='assets/textures/Body_baseColor.png', texture_scale=3,
            **kwargs)

