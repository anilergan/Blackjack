from numpy.random import choice


from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer, QEventLoop

from game_dynamics import BlackjackDynamics


class Play(BlackjackDynamics):

    def __init__(self):
        super().__init__()

        self.countdown = 4
        self.close_card_shown = False


    def initialize_hands(self, players):
        
        for player in players:
            self.hands[player] = []
            # Kurpiyer kendine 2 kart çeker. 
            card = choice(self.deck)
            self.hands[player].append(card)
            card = choice(self.deck)
            self.hands[player].append(card)
        
        self.hands['dealer'] = ['Q', 'A']
        super().update_hand_values()
    
    def hit(self, player = 'seat1'):
        card = choice(self.deck)
        self.hands[player].append(card)

        super().update_hand_values()
    
        





        
        
    



            


