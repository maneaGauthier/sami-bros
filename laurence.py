from ursina import *

from music import MusicLaurence
from player import Player


class Laurence(Entity):
    def __init__(self, player:Player,musicL: MusicLaurence, **kwargs):
        super().__init__(
            player=player,
            model='assets/3D/princess.glb', scale=0.5,
            position=(158, 23, 131),
            color=(255, 203, 154),
            #texture='assets/textures/matis.jpg', texture_scale=0.5,
            origin_y=-.5,
            rotate_y=180,
            **kwargs)
        self.__player = player
        self.__musicL = musicL

    def update(self):
        dist = distance_xz(self.__player.position, self.position)

        hit_info = raycast(self.world_position + Vec3(0, 1, 0), self.forward, 30, ignore=(self,))
        if hit_info.entity == self.__player:
            if dist < 100:
                if not self.__musicL.playing:
                    self.__musicL.play()
            if dist > 150:
                self.__musicL.stop()