from game_gui import Blackjack_GUI

from numpy.random import choice

from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer



class OnePlayerGame(Blackjack_GUI):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        self.players = ['opp1']
        self.player_num = len(self.players)

        self.countdown = 10
        self.ui.stackedwidget_content.setCurrentIndex(1)


    def play(self):

        self.countdown = 2
        self.timer = QTimer(self)

        self.timer.timeout.connect(lambda: self.initialize_announce())
        self.timer.start(1000)


    def initialize_announce(self):
        if self.countdown == 0: 
            self.timer.stop()
            self.reset_chips_image(self.players, True) 
            self.game_on()
        
        self.ui.label_cd.setText(str(self.countdown))
        if self.countdown < 6:
            self.ui.label_announce.setText('Bets are open')
            self.reset_chips_image(self.players, True)
        
        self.countdown -= 1
        print(self.countdown) 
        

    def blackjack_announce(self):
        if self.countdown == 0: 
            self.timer.stop()
            self.reset_chips_image(self.players, True) 
            self.game_on()
        
        self.ui.label_cd.setText(str(self.countdown))

        self.ui.label_announce.setText('Bets are open')
        self.reset_chips_image(self.players, False) 
        self.set_chips_image("dealer", self.players)
        
        self.countdown -= 1
        print(self.countdown) 


    def game_on(self):
        
        self.reset_game_page()
        self.reset_chips_image(self.players, True)

        # Kurpiyer kendine 2 kart çeker. 
        card = choice(self.deck)
        card = 'J'
        self.hands['dealer'].append(card)
        card = choice(self.deck)
        card = 'A'
        self.hands['dealer'].append(card)

        self.display_cards('dealer')
        
        total = self.calculate_hand_value(self.hands['dealer'])
        self.ui.label_dealer_total.setText("{}".format(total))


        # Check BLACKJACK!
        check = self.check_blackjack()
        if check:
            self.countdown = 5
            self.blackjack_announce()



                    




            
            # Oynuncu kart ister (hit) ya da pass geçer (stand).

            


            # Oyuncu kart çektiğinde 21'den büyükse kaybeder.

            # Oyuncu Pass geçtiğinde kurpiyer 16'yı geçinceye kadar kart çeker. 16'yı geçtiğinde durur. Eğer 21'i geçerse yanar.

            # 16'yı geçtiğinde 21'den küçükse ve oyuncuyu da geçmişse kurpiyer kazanır oyuncu kaybeder.
    
