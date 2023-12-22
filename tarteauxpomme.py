from obstructions import Obstructions
from player import Player

class TarteAuxPomme(Obstructions):
    def __init__(self, player: Player, **kwargs):
        super().__init__(
            player=player,
            model='assets/3D/Tarte.obj', scale=1,
            texture='assets/textures/tarte.jpeg', texture_scale=0.5,
            position=(167, 24, 141),
            **kwargs)
        self.__player = player

    def update(self):
        if self.intersects().entity == self.__player:
            list = [
"                    _,.---._                           ,--.-,,-,--,    ,---.              ,-.-.       ,----.                  ,-.-.      _,.---._      .-._                ",
" ,--.-.  .-,--.   ,-.' , -  `.    .--.-. .-.-.        /==/  /|=|  |  .--.'  \      ,--.-./=/ ,/    ,-.--` , \        ,-..-.-./  \==\   ,-.' , -  `.   /==/ \  .-._         ",
"/==/- / /=/_ /   /==/_,  ,  - \  /==/ -|/=/  |        |==|_ ||=|, |  \==\-/\ \    /==/, ||=| -|   |==|-  _.-`        |, \=/\=|- |==|  /==/_,  ,  - \  |==|, \/ /, /        ",
"\==\, \/=/. /   |==|   .=.     | |==| ,||=| -|        |==| ,|/=| _|  /==/-|_\ |   \==\,  \ / ,|   |==|   `.-.        |- |/ |/ , /==/ |==|   .=.     | |==|-  \|  |         ",
" \==\  \/ -/    |==|_ : ;=:  - | |==|- | =/  |        |==|- `-' _ |  \==\,   - \   \==\ - ' - /  /==/_ ,    /         \, ,     _|==| |==|_ : ;=:  - | |==| ,  | -|         ",
"  |==|  ,_/     |==| , '='     | |==|,  \/ - |        |==|  _     |  /==/ -   ,|    \==\ ,   |   |==|    .-'          | -  -  , |==| |==| , '='     | |==| -   _ |         ",
"  \==\-, /       \==\ -    ,_ /  |==|-   ,   /        |==|   .-. ,\ /==/-  /\ - \   |==| -  ,/   |==|_  ,`-._          \  ,  - /==/   \==\ -    ,_ /  |==|  /\ , |         ",
"  /==/._/         '.='. -   .'   /==/ , _  .'         /==/, //=/  | \==\ _.\=\.-'   \==\  _ /    /==/ ,     /          |-  /\ /==/     '.='. -   .'   /==/, | |- |         ",
"  `--`-`            `--`--''     `--`..---'           `--`-' `-`--`  `--`            `--`--'     `--`-----``           `--`  `--`        `--`--''     `--`./  `--`         ",
                    "Bravo Samy vous avez réussi à trouver la tarte aux pommes,Vous pouvez maintenant la déguster pendant votre pause bien méritée."
                    ]

            def win():
                for i in list:
                    print(i)

            quit(print(win()))
