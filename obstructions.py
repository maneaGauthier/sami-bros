from player import Player
from ursina import *


class Obstructions(Entity):
    def __init__(self,player:Player,position ,model,texture,scale, **kwargs):
        super().__init__(
            model=model,
            color=color.gray,
            texture=texture,
            scale=scale,
            collider="box",
            position=position,
            **kwargs
        )
        self.__player = player

