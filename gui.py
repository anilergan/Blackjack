import resources_rc, resources2_rc
from qt import Ui_MainWindow
from game_dynamics import BlackjackDynamics

# Game Dynamis
import ss
from decorators import stand_decorator

# User Interface Libs (PyQt6)
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame, QGroupBox
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QTimer


class BlackjackGUI(QMainWindow, BlackjackDynamics):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
    
        # SIGNAL-SLOTS ------------------------
        # Login Page Buttons
        self.ui.button_one_player_game.clicked.connect(lambda: self.func_button_one_player_game())

        self.ui.button_agent_game.clicked.connect(lambda: self.func_agent_game())
        self.ui.button_agent_game_options_play.clicked.connect(lambda: self.func_agent_game_play())

        self.ui.button_exit.clicked.connect(self.func_button_exit)

        # Game Page Slots
        self.ui.button_hit.clicked.connect(lambda: self.func_hit())
        self.ui.button_stand.clicked.connect(lambda: self.func_stand())
        self.ui.button_double.clicked.connect(lambda: self.func_double())
        self.ui.slider_bet.valueChanged.connect(self.func_bet_slider)

        # Game Page Menu
        self.ui.button_menu.clicked.connect(self.func_menu)
        self.ui.button_reset.clicked.connect(self.func_reset)
        
        self.options_reset()
        self.menu_page()
    


# ---------------------------- PIPELINES ----------------------------

    def pipeline_initialize_game(self):
        self.declare_initial_bankroll()
        self.set_budget()
        self.move_buttons_usability(False)
        self.bet_frame_usabilty(False)
        self.set_lp_board(reset=True)
        self.set_status_board()
        BlackjackDynamics.__init__(self)
        self.game_page()

    def pipeline_reset_game_page(self):
        self.timer.stop()
        BlackjackDynamics.__init__(self)
        # Reset card icons
        self.display_cards(reset=True)
        # Reset boards
        self.set_status_board(reset=True)
        self.set_lp_board(reset=True)
        self.set_bet_box(reset=True)
        self.set_move_box(deactive=True)
        # Reset table
        self.set_total(reset=True)
        self.set_total_and_status(reset=True)
        self.set_budget(reset=True)
        self.set_players_cocktail_and_smoke(reset=True)
        # Reset menu labels
        self.announce(reset=True)
        self.set_chips(reset=True)

    def pipeline_check_blackjack(self):

        self.check_blackjack()
        # Blackjack hand exists
        if 'blackjack' in self.player_status.values():

            # Dealer has Blackjack hand
            if self.player_status['dealer'] == 'blackjack':
                return True

            # It is seat1 vs dealer game and seat1 has blackjack hand while dealer has not.
            elif list(self.player_status.values()).count('blackjack') == 1 and len(self.players) == 2:
                return True

            
            # If it's multiple player game, player takes but game go on.
            elif len(self.players) > 2 and list(self.player_status.values()).count('blackjack') == 1:
                return 
        elif list(self.player_status.values()).count('push') >= 2: return True
        else: return 
    
    def pipeline_init_next_round(self, cd:int=6):
        self.countdown = cd
        self.init_timer(mode='init')

    def pipeline_end_game(self):
        self.close_card_shown = True
        self.display_cards()
        self.set_total()
        self.set_total_and_status()
        self.set_chips(reset=True)
        self.set_bet_box(reset=True)
        self.set_status_board()
        self.set_players_cocktail_and_smoke()
        self.announce()
        self.payout()
        self.set_budget()

# SİGNAL-SLOTS Functions -------------------------------------

    # Menu page Signal-Slots ---------------------------------
    def func_button_one_player_game(self):
        self.game_mode = 'OnePlayerGame'

        self.round = 1

        self.players = ['dealer', 'seat1']
        
        self.bankroll = {
            'dealer': 100000, # a value just for formality
            'seat1': 10
        }

        self.bets = {
            'seat1': 0  
        }

        self.pipeline_initialize_game()
        self.pipeline_init_next_round()
    

    def func_agent_game(self):
        self.options_agent_game()
    
    def func_play_agent_game(self):
        self.mode = self.ui.combobox_agent_game_mode.currentText()
        self.agent = self.ui.combobox_agent_selection.currentText()


    def play_game_agent_vs_dealer(self):
        pass


    def play_agent_game(self):

        

    # Game page Signal-Slots ---------------------------------       
    def func_button_exit(self):
        QApplication.quit()
    
    def func_menu(self):
        self.pipeline_reset_game_page()
        self.menu_page()

    def func_reset(self):
        self.pipeline_reset_game_page()
        if self.game_mode == 'OnePlayerGame':
            self.game_mode = self.func_button_one_player_game()
 
    def func_hit(self, player = 'seat1'):
        if self.ui.button_hit.isEnabled() == True:
            super().hit()
            self.display_cards()
            self.set_total()
            self.set_total_and_status() #it is necessary here, eventhough it will be triggered again in pipeline endgame
            self.update_status()


            if self.hand_values[player] > 21:
                if player == 'seat1': 
                    self.move_buttons_usability(False)
                    self.set_move_box(deactive=True)

                agent = [x for x in self.players if x not in ['dealer', player]]
                if agent: agent = agent[0]
               
                # if agent is bust as well or there is no agent, round ends.
                if len(self.players) == 2 or self.player_status[agent] == 'bust': 
                    self.update_status('dealer', 'win')
                    self.pipeline_end_game()
                    self.pipeline_init_next_round()
                    
                
                # if agent is not 'in play' too.
                elif self.player_status[agent] in ['stand', 'double']:
                    self.countdown = 0
                    self.init_timer(mode='dealer_hit')


                # so agent is still in play
                elif self.player_status[agent] == 'in play':
                    pass
            
                return 'bust'

            else: return 'not bust'

    @stand_decorator
    def func_stand(self, player = 'seat1'):
        self.update_status(player, 'stand')
    
    @stand_decorator
    def func_double(self, player = 'seat1'):
        self.bankroll['seat1'] = self.bankroll['seat1'] - self.bets['seat1'] 
        self.bets[player] = self.bets[player] * 2
        self.set_bet_box()
        self.set_bet_box(deactive=True)
        self.set_chips()
        self.set_budget()

        check_bust = self.func_hit(player)
        if check_bust == 'bust': return 'interrupt'

        self.update_status(player, 'double')

    def func_bet_slider(self, value:int):
        if not 'seat1' in self.players: return

        if self.bankroll['seat1'] < 10 and value > self.bankroll['seat1']:
            self.ui.slider_bet.setValue(self.bankroll['seat1'])
            self.bets['seat1'] = self.bankroll['seat1']
        
        else: 
            self.ui.slider_bet.setValue(value)
            self.bets['seat1'] = value

        self.set_chips()
        self.set_bet_box()

# ------------------------------------------------------------


# UI SUPPORT FUNCTIONS ---------------------------------

    def move_buttons_usability(self, usability:bool):
        if not 'seat1' in self.players:
            self.ui.button_stand.setEnabled(False)
            self.ui.button_hit.setEnabled(False)
            return 

        self.ui.button_stand.setEnabled(usability)
        self.ui.button_hit.setEnabled(usability)
        
        if self.bets['seat1'] > self.bankroll['seat1']:
            self.ui.button_double.setEnabled(False)
        
        else:
            self.ui.button_double.setEnabled(usability)

    def bet_frame_usabilty(self, usability:bool):
        if not 'seat1' in self.players:
            self.ui.slider_bet.setEnabled(False)
            return
        self.ui.slider_bet.setEnabled(usability)
    
    def declare_initial_bankroll(self):
        self.initial_bankroll = {}

        for player, bankroll in self.bankroll.items():
            self.initial_bankroll[player] = bankroll
        
        self.players_total_initial_bankroll = sum([value for player, value in self.initial_bankroll.items() if player != 'dealer'])
        
    def set_budget(self, reset:bool = False):
        if reset:
            for player in self.players:
                if player != 'dealer':
                    label = self.findChild(QLabel, f'label_{player}_budget_amount')
                    label.setText('')
                    label = self.findChild(QLabel, f'label_{player}_budget_dollar')
                    label.setText('')
            
            return

        for player in self.players:
            if player != 'dealer':
                label = self.findChild(QLabel, f'label_{player}_budget_amount')
                label.setText(str(self.bankroll[player]))
                if self.bankroll[player] >= 1:
                    label.setText(str(self.bankroll[player]))
                else:
                    label.setText('')
                label = self.findChild(QLabel, f'label_{player}_budget_dollar')
                if self.bankroll[player] >= 1:
                    label.setText('$')
                else:
                    label.setText('')

    def set_total_and_status(self, reset:bool = False):
        if reset:
            for player in self.players:
                frame = self.findChild(QFrame, f'frame_{player}_total')
                label = self.findChild(QLabel, f'label_{player}_status')
                
                if label: label.setPixmap(QPixmap(""))
                if frame: frame.setStyleSheet('')

            return


        for player, status in self.player_status.items():
            if player == 'dealer': continue
            if status:
                
                frame = self.findChild(QFrame, f'frame_{player}_total')
                label = self.findChild(QLabel, f'label_{player}_status')   

                if status == 'blackjack':
                    icon = QPixmap(":/status/jack.png")
                    frame.setStyleSheet(f"""
                    #frame_{player}_total {{
                    background-color: rgba(29,25,43,50);
                    border-radius: 10px;
                    }}
                    """)
                
                elif status == 'stand':
                    icon = QPixmap(":/deck/stand.png")
                    frame.setStyleSheet(f"""
                    #frame_{player}_total {{
                    background-color: rgba(255,255,255,30);
                    border-radius: 10px;
                    }}""")

                elif status == 'win':
                    icon = QPixmap(f":/status/win.png")
                    frame.setStyleSheet(f"""
                    #frame_{player}_total {{
                    background-color: rgba(212,185,58,30);
                    border-radius: 10px;
                    }}""")

                
                elif status == 'bust':
                    icon = QPixmap(f":/status/lose.png")

                
                elif status == 'double':
                    icon = QPixmap(":/status/double.png")
                    frame.setStyleSheet(f"""
                    #frame_{player}_total{{
                    background-color: rgba(255,255,255,30)
                    border-radius: 10px;
                    }}""")
                
                try: 
                    label.setPixmap(icon)
                except Exception: 
                    print('icon could not assigned! status:', status)
        
    def display_cards(self, reset:bool=False):
        if reset:
            for player in self.players:
                frame = self.findChild(QFrame, f'frame_{player}_cards')
                for label in frame.findChildren(QLabel):
                    label.setPixmap(QPixmap())

            return

        for player in self.players:
            if player != 'dealer':
                for index, card in enumerate(self.hands[player]):
                    icon = QPixmap(f":/cards/{card}.png")
                    label = self.findChild(QLabel, f"label_{player}_card{index+1}")
                    if label: label.setPixmap(icon)      
                     
            elif player == 'dealer' and self.close_card_shown == False:
                for index, card in enumerate(self.hands[player]):
                    if index == 0:
                        icon = QPixmap(f":/cards/{card}.png")
                        label = self.findChild(QLabel, f"label_{player}_card{index+1}")
                        if label: label.setPixmap(icon)
                    elif index == 1:
                        icon = QPixmap(f":/cards/close_card.png")
                        label = self.findChild(QLabel, f"label_{player}_card{index+1}")
                        if label: label.setPixmap(icon)
  
            elif player == 'dealer' and self.close_card_shown:
                for index, card in enumerate(self.hands[player]):
                    icon = QPixmap(f":/cards/{card}.png")
                    label = self.findChild(QLabel, f"label_{player}_card{index+1}")
                    if label: label.setPixmap(icon)
              
    def check_blackjack(self):
        for player in self.players:
            if not 'A' in self.hands[player]: 
                continue
            
            else: 
                total = 0
                for card in self.hands[player]:
                    total += self.card_values[card]

                if total == 21:
                    self.update_status(player = player, status= 'blackjack')
            
    def set_players_cocktail_and_smoke(self, reset:bool = False):
        for player, status in self.player_status.items():
            if player == 'dealer': continue

            if reset or status == 'push':
                martini = self.findChild(QLabel, f'label_{player}_martini')
                martini.setPixmap(QPixmap(""))
            
            elif status in ['win', 'blackjack']:
                martini = self.findChild(QLabel, f'label_{player}_martini')
                martini.setPixmap(QPixmap(":/alcohol/cocktail.png"))
            
            elif status == 'bust':
                martini = self.findChild(QLabel, f'label_{player}_martini')
                martini.setPixmap(QPixmap(":/alcohol/smoke.png"))           
        
    def announce(self, reset:bool = False, game_over:bool = False):

        if reset:
            self.ui.label_announce.setText("")
            self.ui.label_cd.setText("")
            return
        
        elif game_over:
            self.ui.label_announce.setText("Thank you for playing! Game is over.")
            self.ui.label_cd.setText("")
            return
        
        if self.countdown > 0:
            self.ui.label_cd.setText(str(self.countdown))
        else:
            self.ui.label_cd.setText('')
        

        if self.round == 1 and self.countdown >= 5:
            self.ui.label_announce.setText('Welcome! Take your place.')
        
        elif self.countdown >= 5:
            self.ui.label_announce.setText('Round ends!')

        elif list(self.player_status.values()).count(None) == 3 and self.countdown == 0:
            self.ui.label_cd.setText('')
            self.ui.label_announce.setText(f'Round {self.round} has started!')

        elif list(self.player_status.values()).count(None) == 3 and self.countdown <= 4:
            self.ui.label_announce.setText('Bets are open.')
            

        player_bj_list = []
        for player, status in self.player_status.items():
            if status == 'blackjack':
                player_bj_list.append(player)
        if not player_bj_list: return
        
        elif player_bj_list: player_bj_list = [item.capitalize() for item in player_bj_list]

        elif len(player_bj_list) == 1:
            self.ui.label_announce.setText(f'{player_bj_list[0]} blackjack!')
        elif len(player_bj_list) == 2 or len(player_bj_list) == 3:
            announce = ' & '.join(player_bj_list)
            self.ui.label_announce.setText(f'{announce} blackjack!')
                
    def set_status_board(self, reset:bool = False):
        if reset:
            for player in self.players:
                frame = self.findChild(QFrame, f'frame_status_{player}') 
                label = self.findChild(QLabel, f'label_status_{player}')
                frame.setStyleSheet('')
                if label: label.setText('-')
            return
        
        for player in self.players:
            frame = self.findChild(QFrame, f'frame_status_{player}') 
            frame.setStyleSheet(
                """
                QLabel {
	            color: rgba(212,185,58,255);
                }
                """
                )
        try:
            for player, status in self.player_status.items():
                if status:
                    label = self.findChild(QLabel, f'label_status_{player}')
                    label.setText(status)
        except: pass

    def set_lp_board(self, reset:bool = False):
        
        if reset:
            for p in self.players:
                frame = self.findChild(QFrame, f'frame_lp_{p}')
                label_latest = self.findChild(QLabel, f'label_lp_latest_{p}')
                label_total = self.findChild(QLabel, f'label_lp_total_{p}')

                label_latest.setStyleSheet("")
                label_total.setStyleSheet("")
                label_latest.setText('-')
                label_total.setText('-')
                frame.setStyleSheet(
                """
                QLabel {
                color: rgba(212,185,58, 255);
                }
                """
                )
            return

        for player, lp in self.players_lp.items():
            label_latest = self.findChild(QLabel, f'label_lp_latest_{player}')
            label_total = self.findChild(QLabel, f'label_lp_total_{player}')

            label_latest.setText(str(lp))
            if lp < 0: label_latest.setStyleSheet("color: rgba(212, 58, 58, 255)")
            elif lp > 0: label_latest.setStyleSheet("color: rgba(58, 185, 58, 255)")
            else: label_latest.setStyleSheet("color: rgba(212,185,58, 255)")
            
            if player != 'dealer':
                lp_total = self.bankroll[player] - self.initial_bankroll[player]
            else:
                lp_total = self.bankroll['dealer']
            label_total.setText(str(lp_total))
            
            if lp_total < 0: label_total.setStyleSheet("color: rgba(212, 58, 58, 255)")
            elif lp_total > 0: label_total.setStyleSheet("color: rgba(58, 185, 58, 255)")
            else: label_total.setStyleSheet("color: rgba(212,185,58, 255)")

    def set_bet_box(self, reset:bool = False, deactive:bool = False):
        if not 'seat1' in self.players:
            self.ui.groupbox_bet.setStyleSheet('')
            self.ui.label_stake_amount.setText('')
            self.ui.label_stake_dollar.setText('')

        if reset:
            self.ui.groupbox_bet.setStyleSheet('')
            self.ui.label_stake_amount.setText('')
            self.ui.label_stake_dollar.setText('')
            self.ui.label_seat1_stake_amount.setText('')
            self.ui.label_seat1_stake_dollar.setText('')
            return
        
        if deactive:
            self.ui.groupbox_bet.setStyleSheet('')
            self.ui.label_stake_amount.setText(str(self.bets['seat1']))
            self.ui.label_stake_dollar.setText('$')
            return

        bet = self.bets['seat1']

        self.ui.label_stake_amount.setText(str(bet))
        self.ui.label_stake_dollar.setText('$')
        self.ui.groupbox_bet.setStyleSheet(ss.ss_groupbox_bet_active)

        self.ui.label_seat1_stake_amount.setText(str(bet))
        self.ui.label_seat1_stake_dollar.setText('$')

    def set_move_box(self, deactive:bool = False):
        gbox = self.findChild(QGroupBox, 'groupbox_move')
        if deactive:
            gbox.setStyleSheet('')
            return

        gbox.setStyleSheet(ss.ss_groupbox_move_active)
    
    def set_total(self, reset:bool=False):
        if reset:
            for player in self.players:
                frame = self.findChild(QFrame, f'frame_{player}_total')
                label = self.findChild(QLabel, f'label_{player}_total')
                if frame: frame.setStyleSheet("")
                if label: label.setText("")
                frame = self.findChild(QFrame, f'frame_blackjack_text')
                frame.setStyleSheet('')
            return

        for player in self.players:
            if player == 'dealer' and self.close_card_shown == False:
                label = self.findChild(QLabel, f'label_{player}_total')
                open_card = self.hands[player][0]
                open_card_value = self.card_values[open_card]
                label.setText(str(open_card_value))
            elif (player == 'dealer' and self.close_card_shown == True) or (player != 'dealer'):
                total_label = self.findChild(QLabel, f'label_{player}_total')
                total = self.hand_values[player]
                total_label.setText(str(total))
        
        self.update_status()

        for player, status in self.player_status.items():
            if status == 'bust':
                frame = self.findChild(QFrame, f'frame_{player}_total')
                frame.setStyleSheet(
                f"""
                #label_{player}_total {{{ss.ss_label_player_total_bust}}}
                #label_{player}_total_text {{{ss.ss_label_player_total_text_bust}}}
                """
                )

            
            elif status == 'blackjack':
                frame = self.findChild(QFrame, f'frame_blackjack_text')
                frame.setStyleSheet(ss.ss_label_dealer_blackjack)

    def set_chips(self, reset:bool = False):
        if reset:
            for player in self.players:
                if player != 'dealer':
                    label_chips = self.findChild(QLabel, f'label_{player}_chips_image')
                    label_chips.setPixmap(QPixmap(""))
                    label_chips_2 = self.findChild(QLabel, f'label_{player}_chips_image_2')
                    label_chips_2.setPixmap(QPixmap(""))
                    label_count = self.findChild(QLabel, f"label_{player}_chips_count")
                    label_count.setPixmap(QPixmap(""))

            return
            
        for player, bet in self.bets.items():
            chip_label_1 = self.findChild(QLabel, f'label_{player}_chips_image')
            chip_label_2 = self.findChild(QLabel, f'label_{player}_chips_image_2')
            if bet <= 5:
                chip_label_1.setPixmap(QPixmap(f":/chips/chips{bet}.png"))
                chip_label_2.setPixmap(QPixmap(""))
            else: 
                chip_label_1.setPixmap(QPixmap(":/chips/chips5.png"))
                chip_label_2.setPixmap(QPixmap(f":/chips/chips{bet - 5}.png"))
            
            label_bet_count = self.findChild(QLabel, f'label_{player}_chips_count')
            label_bet_count.setText(str(bet))

    def payout(self):
        for player, status in self.player_status.items():

            if player == 'dealer' or status is None: continue

            if status == 'win':
                lp = self.bets[player]
            
            elif status == 'blackjack':
                lp = round(self.bets[player] * 3/2, 1)
                if isinstance(lp, float) and lp.is_integer():
                    lp = int(lp)

            elif status == 'push':
                lp = 0            
            
            else: 
                lp = -self.bets[player]

            self.bankroll[player] += self.bets[player] + lp

            if isinstance(self.bankroll[player], float) and self.bankroll[player].is_integer():
                self.bankroll[player] = int(self.bankroll[player])

            self.players_lp[player] = lp
    
        self.players_lp['dealer'] = -sum([lp for player, lp in self.players_lp.items() if player != 'dealer'])
        
        total_bankroll = sum([value for player, value in self.bankroll.items() if player != 'dealer'])
        self.bankroll['dealer'] = self.players_total_initial_bankroll - total_bankroll
        
        self.set_lp_board()
        for player, bankroll in self.bankroll.items():
            if player == 'dealer': continue
            if bankroll < 1:
                self.update_status(player, 'bankrupt')

    def bankrupt(self):
        for player, status in self.player_status.items():
            if status == 'bankrupt': 
                self.players.remove(player)

                frame = self.findChild(QFrame, f'frame_status_{player}')
                frame.setStyleSheet(
                """
                QLabel {
                color: rgba(212,185,58,100)
                }
                """
                )
                    

# Switch StackWidget Page ------------------------

    def options_reset(self):
        self.ui.stackedwidget_options.setCurrentIndex(0)

    def options_agent_game(self):
        self.ui.stackedwidget_options.setCurrentIndex(1)

    def options_train_agent(self):
        self.ui.stackedwidget_options.setCurrentIndex(2)   

    def menu_page(self):
        self.options_reset()
        self.ui.stackedwidget_content.setCurrentIndex(0)

    def game_page(self):
        self.ui.stackedwidget_content.setCurrentIndex(1)
    





# TIMER and TIMER FUNCTIONS  -------------------------------------------



    def init_timer(self, mode):

        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.handle_timeout(mode))
        
        if not self.timer.isActive():
            self.timer.start(1000)


    def handle_timeout(self, mode):
        if mode == 'init':
            # If user quit game page
            if self.ui.stackedwidget_content.currentIndex() == 0:
                self.timer.stop()
                return 

            if self.countdown == 4:
                self.display_cards(reset=True)
                self.set_total(reset=True)
                self.set_total_and_status(reset=True)

                self.bankrupt()
                if len(self.players) == 1:
                    self.pipeline_reset_game_page()
                    self.announce(game_over=True)
                    self.timer.stop()
                    return
                else:
                    BlackjackDynamics.__init__(self)

                self.func_bet_slider(value=1)
                self.bet_frame_usabilty(True)
                    

            elif self.countdown == 0:
                self.timer.stop()
                self.bankroll['seat1'] = self.bankroll['seat1'] - self.bets['seat1']
                self.set_budget()
                self.init_next_round()


        elif mode == 'dealer_hit':
            if self.player_status['dealer'] == 'in play':
                self.dealer_turn()

            else: 
                self.timer.stop()

        elif mode == 'agent_hit':            
            self.agent_turn()
            
        self.announce()
        self.countdown -= 1
    

    def init_next_round(self):        
        
        self.players_lp = {}
        for player in self.players:
            self.players_lp[player] = 0

        self.round += 1

        if 'seat1' in self.players:
            self.set_move_box()
            self.move_buttons_usability(True)
            self.set_bet_box(deactive=True)
            self.bet_frame_usabilty(False)

        super().initialize_hands(self.players)

        if self.pipeline_check_blackjack():
            self.pipeline_end_game()
            self.pipeline_init_next_round()
        
        else:
            self.set_total()
            self.set_total_and_status(reset=True)
            self.display_cards()
            self.set_chips()

            for player in self.players:
                self.update_status(player=player, status='in play')

            self.set_status_board()
            
    def dealer_turn(self):
        
        if self.close_card_shown: super().hit('dealer')
        else: self.close_card_shown = True

        self.display_cards()
        self.set_total()

        if self.hand_values['dealer'] < 17 and self.countdown == 0:
            self.countdown += 1
            return

        elif self.hand_values['dealer'] >= 17 and self.hand_values['dealer'] <= 21:
            self.update_status('dealer', 'stand') #other player status will be updated as well
            
        elif self.hand_values['dealer'] > 21:
            self.update_status()

        self.timer.stop()
        self.pipeline_end_game()
        self.pipeline_init_next_round()

    def agent_turn(self):



