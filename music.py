from ursina import Audio, held_keys

#from player import player

from player import Player

class MusicAmbiance(Audio):
    def __init__(self):
        super().__init__('assets/audio/Ambiance.mp3', loop=True, autoplay=True)
        self.volume = 0.2

class MusicJump(Audio):
    def __init__(self):
        super().__init__('assets/audio/Jump.mp3', loop=False, autoplay=False)
        self.volume = 1

    def input(self, key):
        if key == 'space':
            if not self.playing:
                self.play()


class MusicWalk(Audio):
    def __init__(self,player:Player):
        super().__init__('assets/audio/Walk.mp3', loop=False, autoplay=False)
        self.volume = 1
        self.__player = player

    def update(self):
        self.volume = 1
        walking = held_keys['a'] or \
                  held_keys['d'] or \
                  held_keys['w'] or \
                  held_keys['s']
        if walking and self.__player.grounded:
            if not self.playing:
                self.play()


class MusicMatis(Audio):
    def __init__(self):
        super().__init__('assets/audio/Annecdote_samy.mp3', loop=False, autoplay=False)
        self.volume = 1

class MusicLaurence(Audio):
    def __init__(self):
        super().__init__('assets/audio/Voiedefin.m4a', loop=False, autoplay=False)
        self.volume = 1