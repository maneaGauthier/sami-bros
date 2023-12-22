from ursina import *
#from ursina.shaders import lit_with_shadows_shader

from enemyATST import EnemyATST
from laurence import Laurence
from matis import Matis
from map import Map
from music import MusicAmbiance, MusicJump, MusicWalk, MusicMatis,MusicLaurence
from obstructionelectricalpanel import ObstructionElectricalPanel
from bossenemy import BossEnemy
from ground import Ground
from nailergun import NailerGun
from player import Player
from obstructionscie import ObstructionScie
from tarteauxpomme import TarteAuxPomme
from timer import Timer

#Entity.default_shader = lit_with_shadows_shader

app = Ursina()  ###############################################################################################################

window.fullscreen = True
map = Map()
ground = Ground()
player = Player()
nailergun = NailerGun()

musicM =MusicMatis()
Matis = Matis(player, musicM)

musicL = MusicLaurence()
Laurence = Laurence(player, musicL)

enemy1 = EnemyATST(player, (98, 0, 15))
enemy2 = EnemyATST(player, (59, 0, 23))
enemy3 = EnemyATST(player, (53, 0, 7))
enemy4 = EnemyATST(player, (64, 0, -3))
enemy5 = EnemyATST(player, (76, 0, -4))
enemy6 = EnemyATST(player, (94, 0, -5))
enemy7 = EnemyATST(player, (75, 0, 9))
enemy8 = EnemyATST(player, (103, -1, 8))
enemy9 = EnemyATST(player, (115, -1, 18))
enemy10 = EnemyATST(player, (129, -1, 13))

boss = BossEnemy(player)

obstacle1  = ObstructionScie(player, (37, 3.5, 36))
obstacle2 = ObstructionScie(player, (45, 3.5, 36))
obstacle3 = ObstructionScie(player, (40, 3.5, 36))
tableauélectrique = ObstructionElectricalPanel(player)
tarteauxpomme = TarteAuxPomme(player)

MusicAmbiance()
MusicJump()
MusicWalk(player)

timer = Timer(duration_minutes=2)
#timer = Timer(duration_seconds=5)
#####################################################################
#from ursina.prefabs import editor_camera
#editor_camera = EditorCamera(enabled=False, ignore_paused=True)
#def pause_input(key):
#   if key == 'tab':  # press tab to toggle edit/play mode
#        editor_camera.enabled = not editor_camera.enabled
#        player.visible_self = editor_camera.enabled
#        player.cursor.enabled = not editor_camera.enabled
#        mouse.locked = not editor_camera.enabled
#        editor_camera.position = player.position
#        application.paused = editor_camera.enabled
#def update():
#   print(player.position)
#pause_handler = Entity(ignore_paused=True, input=pause_input)
#####################################################################
# sun = DirectionalLight()
# sun.look_at(Vec3(1,-1,-1))
Sky()
app.run()  ##################################################################################################################
#