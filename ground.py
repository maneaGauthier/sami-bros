from ursina import *

class Ground(Entity):
    def __init__(self):
        super().__init__(model='plane', collider='mesh', double_sided=True,
                     scale=1000, position=(0, 0, 0),
                    texture_scale=(100,100),
                    texture='wooden_texture.jpg'
                              )


