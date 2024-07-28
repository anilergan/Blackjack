import gui.resources_rc
from gui.blackjack import Ui_MainWindow
from play import Play

# Game Dynamis
import ss

# User Interface Libs (PyQt6)
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame, QGroupBox
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QTimer, QEventLoop, Qt


class BlackjackGUI(QMainWindow, Play):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        # SIGNAL-SLOTS ------------------------
        # Login Page Buttons
        self.ui.button_one_player_game.clicked.connect(lambda: self.func_button_one_player_game(True))

        self.ui.button_exit.clicked.connect(self.func_button_exit)

        # Game Page Slots
        self.ui.button_hit.clicked.connect(lambda: self.func_hit())
        self.ui.button_stand.clicked.connect(lambda: self.func_stand())
        self.ui.button_double.clicked.connect(lambda: self.func_double())
        self.ui.slider_bet.valueChanged.connect(self.func_bet_slider)

        # Game Page Menu
        self.ui.button_menu.clicked.connect(self.func_menu)
        self.ui.button_reset.clicked.connect(self.func_reset)

        self.menu_page()
        
    
# SİGNAL-SLOTS Functions -------------------------------------

    # Menu page Signal-Slots ---------------------------------
    def func_button_one_player_game(self, init:bool = False):

        self.game_mode = 'OnePlayerGame'

        self.round = 0
        

        self.players = ['dealer', 'seat1']
        
        self.bankroll = {
            'seat1': 10
        }

        self.bets = {
            'seat1': 0  
        }

        self.move_buttons_usability(False)
        self.bet_frame_usabilty(False)

        self.pipeline_reset_game_page()
        self.game_page()
        
        self.countdown = 9

        while True:
            self.pipeline_init_next_round(cd=self.countdown)
            check = self.pipeline_check_blackjack()
            if not check: break


    # --------------------------------------------------------


    # Game page Signal-Slots ---------------------------------       
    def func_button_exit(self):
        QApplication.quit()
    

    def func_menu(self):
        self.pipeline_reset_game_page()
        self.menu_page()
        if self.timer: self.timer.stop()


    def func_reset(self):
        self.pipeline_reset_game_page()
        if self.timer: self.timer.stop()

        if self.game_mode == 'OnePlayerGame':
            self.func_button_one_player_game()


    def func_hit(self, player='seat1'):
        if self.ui.button_hit.isEnabled() == True:
            self.ui.button_double.setEnabled(False)
            super().hit()
            super().update_hand_values()
            self.display_cards([player])
            self.set_total()

            if self.hand_values['seat1'] > 21:

                self.set_table()
                self.players_bust.add('seat1')


                if len(self.players_bust) + len(self.players_stand) == len(self.players) - 1 and len(self.players_bust) != len(self.players) - 1:
                    self.countdown = 1
                    self.init_timer(mode='dealer_hit')
                    


                elif len(self.players_bust) + len(self.players_stand) == len(self.players) - 1 and len(self.players_bust) == len(self.players) - 1: 
                    self.announce()
                    self.set_table() 


                self.move_buttons_usability(False)

                # initialize new round
                self.countdown = 4
                self.init_timer('init')

                if self.ui.stackedwidget_content.currentIndex() == 0: return

                self.init_next_round()
                    
        else: 
            return


    def func_stand(self, player = 'seat1'):
        if self.ui.button_hit.isEnabled() == True:
            self.players_stand.add(player)
            self.set_table()
            
            if len(self.players_bust) + len(self.players_stand) == len(self.players) - 1:
                self.countdown = 1
                self.init_timer(mode='dealer_hit')
                if self.ui.stackedwidget_content.currentIndex() == 0: 
                    return

            self.move_buttons_usability(False)

            # initialize new round
            self.countdown = 4
            self.init_timer('init')
            if self.ui.stackedwidget_content.currentIndex() == 0: return
 
                
                
        else: 
            return

    
    def func_bet_slider(self, value):
        if self.bankroll['seat1'] < 10:
            self.ui.slider_bet.setMaximum(self.bankroll['seat1'])
        
        else: 
            self.ui.slider_bet.setMaximum(10)

        self.bets['seat1'] = value
        self.ui.label_stake_amount.setText(str(value))
        self.bets['seat1'] = value
        self.set_chips()

        
        budget = self.bankroll['seat1'] - self.bets['seat1']
        
        self.ui.label_seat1_budget_amount.setText(str(budget))
    
    # --------------------------------------------------------


# UI SUPPORT FUNCTIONS ---------------------------------

    def init_next_round(self):
            Play.__init__(self)
            
            self.round += 1
            self.ui.label_round_number.setText(str(self.round))
            self.players = ['dealer', 'seat1']
            
            self.move_buttons_usability(True)

            super().initialize_hands(self.players)

            self.display_cards(self.players)
            self.set_total()
     
            self.set_chips()

            for player in self.players:
                self.update_status(player=player, status='in play')
            

    def init_timer(self, mode):
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.handle_timeout(mode))
        self.runtime_actions()


    def runtime_actions(self):
        self.event_loop = QEventLoop()
        self.timer.start(1000)
        self.event_loop.exec()


    def handle_timeout(self, mode):
        if mode == 'init':
            # If user quit game page
            if self.ui.stackedwidget_content.currentIndex() == 0:
                self.timer.stop()
                self.event_loop.quit()
                return
            
            if self.countdown == 5:
                self.set_table()
                self.set_bet_box()
                self.bet_frame_usabilty(True)

            elif self.countdown == 0:
                self.set_bet_box(deavtive=True)
                self.set_move_box()
                self.bet_frame_usabilty(False)
                self.timer.stop()
                self.event_loop.quit()

            self.announce()

            


        elif mode == 'dealer_hit':
            if self.ui.stackedwidget_content.currentIndex() == 0:
                self.timer.stop()
                self.event_loop.quit()
                return
            
            self.dealer_turn()

        elif mode == 'players_hit':
            if self.ui.stackedwidget_content.currentIndex() == 0:
                self.timer.stop()
                self.event_loop.quit()
                return
            
            self.opponent_turn()


        if mode != 'init' and self.countdown == 1: self.countdown -= 1
        elif mode == 'init': self.countdown -= 1

 
    def move_buttons_usability(self, usability:bool):
        self.ui.button_stand.setEnabled(usability)
        self.ui.button_hit.setEnabled(usability)
        
        if self.bets['seat1'] > self.bankroll['seat1']:
            self.ui.button_double.setEnabled(False)
        
        else:
            self.ui.button_double.setEnabled(usability)

    
    def bet_frame_usabilty(self, usability:bool):
        self.ui.slider_bet.setEnabled(usability)


    def set_table(self, reset:bool = False):

        if reset:
            for player in self.players:
                frame = self.findChild(QFrame, f'frame_{player}_total')
                label = self.findChild(QLabel, f'label_{player}_status')
                
                if label: label.setPixmap(QPixmap(""))
                
                if frame:
                    frame.setStyleSheet(
                    """
                    """
                    )
                
                if player != 'dealer':
                    label = self.findChild(QLabel, f'label_{player}_budget_amount')
                    label.setText('')
                    
                    label = self.findChild(QLabel, f'label_{player}_budget_dollar')
                    label.setText('')

            return
    
        for player in self.players:
            if player != 'dealer':
                label = self.findChild(QLabel, f'label_{player}_budget_amount')
                label.setText(str(self.bankroll[player] - self.bets[player]))

                label = self.findChild(QLabel, f'label_{player}_budget_dollar')
                label.setText('$')


        for player, status in self.player_status.items():
            if status:
                frame = self.findChild(QFrame, f'frame_{player}_total')
                label = self.findChild(QLabel, f'label_{player}_status')   

                if status == 'blackjack':
                    icon = QPixmap(":/status/jack.png")
                    frame.setStyleSheet(
                    f"""
                    #frame_{player}_total {{
                    background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(29,25,43,100), stop:0.75 transparent);
                    border-radius: 10px;
                    }}
                    """
                    )
                
                elif status == 'stand':
                    icon = QPixmap(":/icons/lose.png")
                    frame.setStyleSheet(
                    f"""
                    #frame_{player}_total {{
                    background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255,255,255,100), stop:0.75 transparent);
                    border-radius: 10px;
                    }}
                    """
                    )

                elif status == 'win' or status == 'double_win':
                    icon = QPixmap(f":/status/win.png")
                    frame.setStyleSheet(
                    f"""
                    #frame_{player}_total {{
                    background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(212,185,58,100), stop:0.75 transparent);
                    border-radius: 10px;
                    }}
                    """
                    )
                
                elif status == 'push':
                    icon = QPixmap(f":/status/push.png")
                    frame.setStyleSheet(
                    f"""
                    #frame_{player}_total {{
                    background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(43,148,242,100), stop:0.75 transparent);
                    border-radius: 10px;
                    }}
                    """
                    ) 
                
                elif status == 'bust' or status == 'double_bust':
                    icon = QPixmap(f":/status/lose.png")
                    frame.setStyleSheet(
                    f"""
                    #frame_{player}_total {{
                    background-color:  qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(29,25,43,100), stop:0.75 transparent);
                    border-radius: 10px;
                    }}
                    """
                    )
                
                elif status == 'double':
                    icon = QPixmap(":/icons/lose.png")
                    frame.setStyleSheet(
                    f"""
                    #frame_{player}_total {{
                    background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(166,42,53,100), stop:0.75 transparent);
                    border-radius: 10px;
                    }}
                    """
                    )


    def display_cards(self, reset:bool=False,  show_close_card:bool=False):
        if reset:
            for player in self.players:
                frame = self.findChild(QFrame, f'frame_{player}_cards')
                for label in frame.findChildren(QLabel):
                    label.setPixmap(QPixmap())

                total_label = self.findChild(QLabel, f'label_{player}_total')
                total_label.setText('')


        for hand in self.players:
            if hand == 'dealer' and len(self.hands[hand]) == 2 and show_close_card == False:
                for index, card in enumerate(self.hands[hand]):
                    if index == 0:
                        icon = QPixmap(f":/cards/{card}.png")
                        label = self.findChild(QLabel, f"label_{hand}_card{index+1}")
                        if label: label.setPixmap(icon)
                    elif index == 1:
                        icon = QPixmap(f":/cards/close_card.png")
                        label = self.findChild(QLabel, f"label_{hand}_card{index+1}")
                        if label: label.setPixmap(icon)

            
            else:
                for index, card in enumerate(self.hands[hand]):
                    icon = QPixmap(f":/cards/{card}.png")
                    label = self.findChild(QLabel, f"label_{hand}_card{index+1}")
                    if label: label.setPixmap(icon)
        

    def check_blackjack(self):
        for player in self.players:
            if 'A' not in self.hands[player]: 
                continue
            
            else: 
                total = 0
                for card in self.hands[player]:
                    if card != 'A':
                        total += self.card_values[card]
                    else: 
                        total += 11 # A is 11 here.
                if total == 21:
                    self.update_status(player = player, status= 'blackjack')
            
   
    def set_players_cocktail_and_smoke(self, reset:bool = False):
        for player, status in self.player_status.items():
            if reset or status == 'push':
                martini = self.findChild(QLabel, f'label_{player}_martini')
                martini.setPixmap(QPixmap(""))
            
            elif status == 'win' or 'blackjack' or 'double_win':
                martini = self.findChild(QLabel, f'label_{player}_martini')
                martini.setPixmap(QPixmap(":/alcohol/cokctail.png"))
            
            elif status == 'bust':
                martini = self.findChild(QLabel, f'label_{player}_martini')
                martini.setPixmap(QPixmap(":/alcohol/smoke.png"))           
        

    def announce(self, reset:bool = False):

        if reset:
            self.ui.label_announce.setText("")
            self.ui.label_cd.setText("")
            return
        
        self.ui.label_cd.setText(str(self.countdown))
        
        if list(self.player_status.values()).count(None) == 3 and self.countdown > 5:
            self.ui.label_announce.setText('Welcome! Take your place.')

        elif list(self.player_status.values()).count(None) == 3 and self.countdown <= 5:
            self.ui.label_announce.setText('Bets are open.')
            
        
        elif self.player_status['dealer'] != 'blackjack':
            self.ui.label_cd.setText('')
            r = self.ui.label_round_number.text()
            self.ui.label_announce.setText(f'Round {r} has started!')
            

        elif [self.player_status[player] for player in self.players].count(None) == 0:
            self.ui.label_announce.setText('Round ends!')

        for player, status in self.player_status.items():
            if player == 'dealer' and status == 'blackjack':
                self.ui.label_announce.setText('Dealer Blackjack!')
        

    def set_status_board(self, reset:bool = False):
        if reset:
            for player in self.players:
                frame = self.findChild(QFrame, f'frame_status_{player}') 
                frame.setStyleSheet(
                """
                QLabel {
	            color: rgba(212,185,58, 200)
                }
                """
                )

                label = self.findChild(QLabel, f'label_status_{player}')
                label.setText('-')
            return

        for player, status in self.player_status.items():
            if status:
                frame = self.findChild(QFrame, f'frame_status_{player}') 
                frame.setText(status.capitalize())
    

    def set_lp_board(self,reset:bool = False):
        if reset:
            for player in self.players:
                frame = self.findChild(QFrame, f'frame_lp_{player}') 
                frame.setStyleSheet(
                """
                QLabel {
	            color: rgba(212,185,58, 200)
                }
                """
                )
            return

        # BURAYA LP GÜNCELLEME GELECEK


    def set_bet_box(self, reset:bool = False, deavtive:bool = False):

        if reset:
            self.ui.groupbox_bet.setStyleSheet('')
            self.ui.label_stake_amount.setText('')
            self.ui.label_stake_dollar.setText('')
            print('Bet board reset!')
            return
        
        if deavtive:
            self.ui.groupbox_bet.setStyleSheet('')
            self.ui.label_stake_amount.setText(str(self.bets['seat1']))
            self.ui.label_stake_dollar.setText('$')
            print('Bet board deactivated!')
            return

        if self.ui.label_stake_amount.text() == '': self.func_bet_slider(1)
        self.ui.label_stake_dollar.setText('$')
        self.ui.groupbox_bet.setStyleSheet(ss.ss_groupbox_bet_active)
        

    def set_move_box(self, reset:bool = False):
        if reset:
            gbox = self.findChild(QGroupBox, 'groupbox_move')
            gbox.setStyleSheet('')
            return

        self.ui.groupbox_move.setStyleSheet(ss.ss_groupbox_move_active)


    def set_total(self, include_close_card:bool=False):
        for player in self.players:
            if player == 'dealer' and len(self.hands['dealer']) == 2 and include_close_card == False:
                label = self.findChild(QLabel, f'label_{player}_total')
                open_card = self.hands[player][0]
                open_card_value = self.card_values[open_card]
                label.setText(f"{open_card_value}")
            else: 
                total_label = self.findChild(QLabel, f'label_{player}_total')
                total = self.hand_values[player]
                total_label.setText(f"{total}")


    def set_chips(self, reset:bool = False):
        if reset:
            for player in self.players:
                if player != 'dealer':
                    label = self.findChild(QLabel, f'label_{player}_chips_image')
                    label.setPixmap(QPixmap(""))
            return
            

        for player in self.players:
            if player != 'dealer':
                chip_label_1 = self.findChild(QLabel, f'label_{player}_chips_image')
                chip_label_2 = self.findChild(QLabel, f'label_{player}_chips_image_2')
                if self.bets[player] <= 5:
                    chip_label_1.setPixmap(QPixmap(f":/chips/chips{self.bets[player]}.png"))
                    chip_label_2.setPixmap(QPixmap(""))
                else: 
                    chip_label_1.setPixmap(QPixmap(":/chips/chips5.png"))
                    chip_label_2.setPixmap(QPixmap(f":/chips/chips{self.bets[player] - 5}.png"))
        

        for player, status in self.player_status.items():
            if status == 'blackjack':
                label = self.findChild(QLabel, f'label_{player}_chips_image')
                label.setPixmap(QPixmap("")) 
        

    def dealer_turn(self):

        if self.hand_values['dealer'] < 17 and self.countdown == 0:
            self.countdown += 1
        

        elif self.countdown == 0:
            self.timer.stop()
            self.event_loop.quit()
            return
        

        elif self.hand_values['dealer'] >= 17 and self.hand_values['dealer'] < 21:
            highest_hand = 0
            winner_list = []
            for player in self.players:
                if self.hand_values[player] >= highest_hand and self.hand_values[player] <= 21:
                    highest_hand = self.hand_values[player]
                    winner_list.append(player)
                
            self.announce()
            self.set_table()

            self.init_next_round()
            return

                

        elif self.hand_values['dealer'] == 21:
            blackjack_hands = []
            for player in self.players:
                if self.hand_values[player] == 21:
                    blackjack_hands.append(player)

            if len(blackjack_hands) == 1:
                self.announce(winner=['dealer'])
            
            else:
                winner_list = []
                for player in blackjack_hands:
                    if len(self.hands[player]) == 2:
                        winner_list.append(player)
                        self.announce(winner=winner_list)

                    else: self.announce()
            
            self.init_next_round()
            return


        elif self.hand_values['dealer'] > 21:
            highest_hand = 0
            winner_list = []
            for player in self.players:
                if self.hand_values[player] >= highest_hand and self.hand_values[player] <= 21:
                    highest_hand = self.hand_values[player]
                    winner_list.append(player)

            self.announce(winner=winner_list)

            self.init_next_round()
            return
        
        if self.close_card_shown:
            super().hit('dealer')
            super().update_hand_values()
            self.display_cards(['dealer'], True)
            self.set_total(True)

        
        else:
            self.display_cards(['dealer'], True)
            self.set_total(True)
            
            self.close_card_shown = True
             
    
    def menu_page(self):
        self.ui.stackedwidget_content.setCurrentIndex(0)


    def game_page(self):
        self.ui.stackedwidget_content.setCurrentIndex(1)


    def payout(self):
        for player, status in self.player_status.items():
            if status == 'win' or 'double win':
                # $10 -> $10 + initial
                profit = self.bets[player] + self.bets[player]
                self.bankroll[player] = profit

            
            elif status == 'blackjack':
                # $10 -> $15 + initial
                profit = self.bets[player] * 3/2 + self.bets[player]
                self.bankroll[player] = profit
            
            elif status == 'push':
                # initial
                profit = self.bets[player]
                self.bankroll[player] = profit

            if status:
                label = self.findChild(QLabel, f'label_{player}_budget_amount')
                label.setText(str(self.bankroll[player]))
    
    
    # Multiple Player Game Functions ------------------------
    
    def opponent_turn(self, player:str):
        if self.countdown == 0:
            self.timer.stop()
            self.event_loop.quit()
            return
        
        if player not in self.players_bust:
            super().hit(player)
            super().update_hand_values()
            self.display_cards([player])
            self.set_total()


            if self.hand_values[player] > 21:
                self.players_bust.add(player)
                self.set_table(bust=player)
    

    def opponent_bet(self):
        pass
        
    
    # PIPELINES ---------------------------------------

    def pipeline_init_next_round(self, cd:int=4):
        self.countdown = cd
        self.init_timer(mode='init')
        if self.ui.stackedwidget_content.currentIndex() == 0: return
        self.bankroll['seat1'] = self.bankroll['seat1'] - self.bets['seat1']
        self.init_next_round()
    

    def pipeline_end_game(self):
        self.set_table()
        self.set_players_cocktail_and_smoke()
        self.set_status_board()
        self.payout()


    def pipeline_check_blackjack(self):
        self.check_blackjack()

        # Blackjack hand exists
        if 'blackjack' in self.player_status.values():
            # Figure out these seperetaly
                # If dealer blackjack
                # if players blackjack


            # Dealer has Blackjack hand
            if self.player_status['dealer'] == 'blackjack':
                self.pipeline_end_game()
                return True
            
            # If it's multiple player game, player takes but game go on.
            elif list(self.player_status.values()).count('blackjack') < len(self.players) - 1:
                return False
            
            # If it's one player game round ends, player takes.
            else: 
                 self.pipeline_end_game()
                 return True


        else:
            return False

        # Blackjack hand does not exists

            # Game go on


    def pipeline_reset_game_page(self):
        # Reset card icons
        self.display_cards(reset=True)
        
        # Reset boards
        self.set_lp_board(reset=True)
        self.set_status_board(reset=True)
        self.set_bet_box(reset=True)
        self.set_move_box(reset=True)

        # Reset table
        self.set_table(reset=True)
        
        # Reset menu labels
        self.announce(reset=True)
        self.set_chips(reset=True)