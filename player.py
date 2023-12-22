from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


class Player(FirstPersonController):
    def __init__(self):
        super().__init__(
            model='cube',
            color=color.rgb(255,203,154),
            speed=15,
            jump_height=10,
            collider='mesh',
            scale=(1, 2, 1),
            position=(-3,0,0),
            #position = (116.997, 22.0177, 42.2662),
            visible_self=False,
            gravity=2,
            rotation=(0,85,0)
        )
        camera.fov = 110

    pause_handler = Entity(ignore_paused=True)
    #pause_text = Text('PAUSED', origin=(0, 0), scale=2, enabled=False)
    def pause_handler_input(key):
        if key == 'escape':
            application.paused = not application.paused  # Pause/unpause the game.
            mouse.locked = not application.paused
    pause_handler.input = pause_handler_input  # Assign the input function to the pause handler.







