from ursina import *
from player import Player
from music import MusicMatis

class Matis(Entity):
    def __init__(self, player:Player,musicM: MusicMatis, **kwargs):
        super().__init__(
            player=player,
            model='cube', scale=(1,8,1),
            position=(51, 0, 2),
            texture='assets/textures/matis.jpg', texture_scale=0.5,
            origin_y=-.5,
            **kwargs)
        self.__player = player
        self.__musicM = musicM
    def update(self):
        dist = distance_xz(self.__player.position, self.position)
        self.look_at_2d(self.__player.position, 'y')
        hit_info = raycast(self.world_position + Vec3(0, 1, 0), self.forward, 30, ignore=(self,))
        if hit_info.entity == self.__player:
            if dist < 5:
                if not self.__musicM.playing:
                    self.__musicM.play()
            if dist > 10:
                self.__musicM.stop()

