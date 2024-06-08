from game import Blackjack
from OnePlayerGame import OnePlayerGame

class Play(Blackjack):
    def __init__(self):
        if mode == "OnePlayerGame":
            game_obj = OnePlayerGame()
            game_obj.play()
