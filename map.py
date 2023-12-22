from ursina import *
class Map(Entity):
    def __init__(self):
        super().__init__(model="assets/3D/mapv8.obj",
                              collider='mesh',
                            double_sided=True,
                              scale=(30,60,30),
                              texture='wall.jpg',
                              texture_scale=10,
                              position=(0,0,0),
                            rotation=(0,180,0),
                              )
