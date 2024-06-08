import numpy as np
import sys

# sys.path.append("tic-tac-toe-dp//gui")
from gui.blackjack import Ui_MainWindow
import gui.resources_rc

# Game Dynamis

# User Interface Libs (PyQt6)
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QTimer



class BlackjackGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        # SIGNAL-SLOTS ------------------------
        # Login Page Buttons
        self.ui.button_one_player_game.clicked.connect(self.func_button_one_player_game)


        # Game Page Slots
        self.ui.button_hit.clicked.connect(self.func_hit)
        self.ui.button_stand.clicked.connect(self.func_hit)

        # Game Page Menu
        self.ui.button_menu.clicked.connect(self.func_menu)
        self.ui.button_reset.clicked.connect(self.func_reset)

        self.init_page()
        
    
    # SİGNAL-SLOTS Functions
    def func_button_one_player_game(self):
        self.game_mode = 'one_player_game' 
        from OnePlayerGame import OnePlayerGame
        play_obj = OnePlayerGame(self.ui)
        play_obj.play()


    # UI SUPPORT FUNCTIONS ---------------------------------
    def reset_game_page(self):
        for frame in [self.ui.frame_dealer, self.ui.frame_agent, self.ui.frame_opp1, self.ui.frame_opp2]:
            for label in frame.findChildren(QLabel):
                label.setPixmap(QPixmap())  # Boş bir pixmap ile ikonu silmek için

                for label in [self.ui.label_dealer_total, self.ui.label_agent_total, self.ui.label_opp1_total, self.ui.label_opp2_total]:
                    label.setText("")
        
        self.ui.label_announce.setText("")
        self.ui.label_cd.setText("")

            
        self.ui.stackedwidget_content.setStyleSheet(
        """
        #page_1_menu {
            background-color: rgba(59,82,63,255);
        }
        #page_2_game {
            background-color: rgba(52,14,16,255);
        }
        """
        )

        self.ui.frame_dealer.setStyleSheet(
        """
        #frame_dealer * {
        background-color: transparent;
        }

        """
        )
    
        self.ui.frame_dealer_total.setStyleSheet(
        """
        #frame_dealer_total * {
        background-color: transparent;
        color: rgba(212,185,58,255);
        }
        """
        )
    
    def blackjack(self):
        self.ui.stackedwidget_content.setStyleSheet(
            """
            #page_1_menu {
                background-color: rgba(59,82,63,255);
            }
            #page_2_game {
                background-color: rgba(52,14,16,255);
                background-color: black;
            }
            """
            )

        self.ui.frame_dealer.setStyleSheet(
            """
            #frame_dealer * {
            background-color: transparent;
            }

            #frame_dealer {
            background-color: black;
            }
            """
            )
        
        self.ui.frame_dealer_total.setStyleSheet(
            """
            #frame_dealer_total * {
            background-color: transparent;
            color: rgba(212,185,58,255);
            }

            #frame_dealer_total {
            background-color: black;
            }
            """
            )

        self.ui.label_announce.setText("BLACKJACK!")


    def display_cards(self, hand):
        for index, card in enumerate(self.hands[hand]):
            print('Card: ', card)
            icon = QPixmap(f":/cards/{card}.png")
            label = self.findChild(QLabel, f"label_dealer_card{index+1}")
            if label: label.setPixmap(icon)

    def countdown(self, sec):
        return [i for i in range(sec, 1, -1)]
    
    def check_blackjack(self):
        if 'A' not in self.hands['dealer']: return False
        else: 
            total = 0
            for card in self.hands['dealer']:
                if card != 'A':
                    total += self.card_values[card]
                else: 
                    total += 11 # A is 11 here.
            if total == 21: return True
            else: return False
    
    def calculate_hand_value(self, hand):
        ace_num = hand.count('A')
        total = 0
        for card in hand:
            total += self.card_values[card]
            if total > 21 and ace_num != 0:
                total -= 10
                ace_num -= 1
        
        return total


    def set_chips_image(self, winner, losers):
        winners_label = self.findChild(QLabel, f'label_{winner}_chips_image')
        winners_label.setPixmap(QPixmap(":/chips/wins_chips.png"))

        for loser in losers:
            losers_label = self.findChild(QLabel, f'label_{loser}_chips_image')
            losers_label.setPixmap(QPixmap(""))
    

    def reset_chips_image(self, players, bets):
        if not bets: 
            for player in players:
                player_label = self.findChild(QLabel, f'label_{player}_chips_image')
                player_label.setPixmap(QPixmap(""))

        else: 
            for player in players:
                player_label = self.findChild(QLabel, f'label_{player}_chips_image')
                player_label.setPixmap(QPixmap(":/chips/chips.png"))
    
    
    def init_page(self):
        self.ui.stackedwidget_content.setCurrentIndex(0)



    # PLAY FUNCTİONS ----------------------------------

    def func_hit(self):
        pass

    def func_stand(self):
        pass


    def func_menu(self):
        self.reset_game_page()
        self.reset_chips_image(self.players, False)
        self.init_page()

    def func_reset(self):
        self.reset_game_page()
        self.reset_chips_image(self.players, False)

        if self.game_mode == 'one_player_game':
            self.func_button_one_player_game()
        

