import traceback
from PySide6.QtGui import (
    QPixmap, 
    QColor, 
    QCursor
    )

# User Interface Libs (PyQt6)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGroupBox,
    QLabel,
    QSpinBox,
    QListWidgetItem,
    QSizePolicy,
    QHBoxLayout,
    QPushButton
    )

from PySide6.QtCore import (
    QSize,
    Qt
    )

# Game Dynamis
import ss

def grad_condition_spinbox_color(checked, self, spinbox_name):
    spbox = self.findChild(QSpinBox, spinbox_name)
    if checked:
        spbox.setStyleSheet(
        """
        color: rgba(32,139,228,255);
        background-color: rgba(32,139,228,0.1);
        """
        ) 
    else:
        spbox.setStyleSheet("")

def next_round_button_usability(self, usability:bool=True):
    self.ui.button_next_round.setEnabled(usability)
    if usability:
        self.ui.button_next_round.setStyleSheet(ss.ss_button_next_round_active)
    else: 
        self.ui.button_next_round.setStyleSheet(ss.ss_button_next_round_deactive)

def move_buttons_usability(self, usability:bool=True):
    self.ui.button_stand.setEnabled(usability)
    self.ui.button_hit.setEnabled(usability)
    try:
        if self.game_mode in ["MultiAgentGame", "TrainAgent"]:
            self.ui.button_double.setEnabled(False)
            return
        if self.bets['seat1'] > self.bankroll['seat1']:
            self.ui.button_double.setEnabled(False)
        else:
            self.ui.button_double.setEnabled(usability)
        if usability:
            self.ui.groupbox_move.setStyleSheet(ss.ss_groupbox_move_active)
            QApplication.processEvents()
        else: 
            gbox = self.findChild(QGroupBox, 'groupbox_move')
            gbox.setStyleSheet('')
    except Exception:
        pass

def bet_frame_usabilty(self, usability:bool):
    self.ui.slider_bet.setEnabled(usability)
    if usability:
        self.ui.slider_bet.setValue(1)
        self.bets["seat1"] = 1
        self.ui.label_stake_amount.setText('$'+str(1))
        set_chips(self)
        set_bet_box(self)
    elif self.game_mode in ["OnePlayerGame", "SingleAgentGame"]:
        set_bet_box(self, deactive=True)

def set_budget(self, reset:bool = False):
    if reset:
        for player in self.players:
            if player != 'dealer':
                label = self.findChild(QLabel, f'label_{player}_budget_amount')
                label.setText('')
        return

    for player in self.players:
        if player != 'dealer':
            if not self.player_status[player] == "double":
                current_budget = self.bankroll[player] - self.bets[player]
            else:
                current_budget = self.bankroll[player] 
            label = self.findChild(QLabel, f'label_{player}_budget_amount')
            label.setText('$'+str(current_budget))

def set_status_icon(self, player=None, reset:bool = False):
    if reset:
        for player in self.players:
            label_status = self.findChild(QLabel, f'label_{player}_status')
            label_total = self.findChild(QLabel, f'label_{player}_total')
            if label_status: 
                label_status.setPixmap(QPixmap(""))
            if label_total: 
                label_total.setStyleSheet('')
        return

    if player:
        check_blackjack_push = list(self.hand_values.values()).count(21) > 1
        status = self.player_status[player]
        if status:
            label_status = self.findChild(QLabel, f'label_{player}_status')   
            label_total = self.findChild(QLabel, f'label_{player}_total')
            icon = None

            if status == 'blackjack' or (status == 'push' and check_blackjack_push):
                icon = QPixmap(":/icons/blackjack.png")
                
            elif status == 'stand':
                icon = QPixmap(":/icons/stand.png")

            elif status == 'win':
                icon = QPixmap(":/icons/wins_chips.png")

            elif status == 'push':
                icon = QPixmap(":/icons/push.png")
            
            elif status == 'bust':
                icon = QPixmap(":/icons/lose.png")
                label_total.setStyleSheet(f"""
                    #label_{player}_total {{
                    border-radius: 10px;
                    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0), stop: 0.7 rgba(212, 53, 87,25), stop:0.85 rgba(212, 53, 87,50), stop:1 rgba(212, 53, 87,75));
                    border:1 solid rgb(212, 53, 87);
                    }}
                """
                )

            elif status == "lose":
                icon = QPixmap(":/icons/lose.png")
            
            elif status == 'double':
                icon = QPixmap(":/icons/double.png")
            
            elif status == "bankrupt":
                icon = QPixmap(":/icons/bankrupt.png")

            try:
                if icon:
                    label_status.setPixmap(QPixmap(icon))
            except UnboundLocalError: 
                traceback.print_exc()
                raise UnboundLocalError('Icon could be assigned.')

def display_cards(self, reset:bool=False, player=None):
    if reset:
        for player in self.players:
            frame = self.findChild(QFrame, f'frame_{player}_cards')
            for label in frame.findChildren(QLabel):
                if label.objectName().startswith(f"label_{player}_card"): 
                    label.setPixmap(QPixmap(""))

            total_label = self.findChild(QLabel, f'label_{player}_total')
            total_label.setText('')
        return

    # for player in self.players:
    if player == 'dealer' and not self.dealer_close_card_shown:
        for index, card in enumerate(self.hands[player]):
            if index == 0:
                icon = QPixmap(f":/cards/{card}.png")
                label = self.findChild(QLabel, f"label_{player}_card{index+1}")
                if label: label.setPixmap(icon)
            elif index == 1:
                icon = QPixmap(":/cards/close_card.png")
                label = self.findChild(QLabel, f"label_{player}_card{index+1}")
                if label: 
                    label.setPixmap(icon)

    else:
        for index, card in enumerate(self.hands[player]):
            icon = QPixmap(f":/cards/{card}.png")
            label = self.findChild(QLabel, f"label_{player}_card{index+1}")
            if label:
                label.setPixmap(icon)


def check_blackjack(self):
    blackjack_hands = set()
    for player in self.players:
        total = 0
        for card in self.hands[player]:
            total += self.CARD_VALUES[card]
        if total == 21 and len(self.hands[player]) == 2:
            blackjack_hands.add(player)
    return blackjack_hands


def set_cocktail_and_smoke(self, reset:bool = False):
    for player, status in self.player_status.items():
        if player == 'dealer': 
            continue
        if reset or status == 'push':
            martini = self.findChild(QLabel, f'label_{player}_martini')
            martini.setPixmap(QPixmap(""))
        
        elif status == 'win' or status == 'blackjack':
            martini = self.findChild(QLabel, f'label_{player}_martini')
            martini.setPixmap(QPixmap(":/icons/cocktail.png"))
        
        elif status == 'bust' or status == 'lose':
            martini = self.findChild(QLabel, f'label_{player}_martini')
            martini.setPixmap(QPixmap(":/icons/smoke.png"))           
    
def announce(self, reset:bool = False, subject:str = None):
    if reset:
        self.ui.label_announce.setText("")
        self.ui.label_cd.setText("")
        return

    if self.game_mode != "TrainAgent" and subject == 'game over':
        self.ui.label_announce.setText(f"{self.bankrupt_player.capitalize()} bankrupt... Bets are closed.")
        self.ui.label_cd.setText("")
        return

    elif self.game_mode != "TrainAgent" and subject == 'round ends':
        self.ui.label_announce.setText(f"Round {self.round} ends!")
        self.ui.label_cd.setText("")
        return

    
    if self.game_mode != "TrainAgent":
        self.ui.label_cd.setText(str(self.countdown))
        
        if self.countdown > 3:
            self.ui.label_announce.setText('Welcome! Take your place.')

        elif self.countdown <= 3 and self.countdown > 0:
            self.ui.label_announce.setText('Bets are open.')
            
        
        elif self.player_status['dealer'] != 'blackjack':
            self.ui.label_cd.setText('')
            self.ui.label_announce.setText(f'Round {self.round} has started!')
            

        elif [self.player_status[player] for player in self.players].count(None) == 0:
            self.ui.label_announce.setText('Round ends!')

        for player, status in self.player_status.items():
            if player == 'dealer' and status == 'blackjack':
                self.ui.label_announce.setText('Dealer Blackjack!')
    else:
        self.ui.label_cd.setText(self.train_timer_text)


def set_status_board(self, player=None, reset:bool=False):
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
            label.setText(f'{player}: -')
        return
    if player:
        status = self.player_status[player]
        if status:
            label = self.findChild(QLabel, f'label_status_{player}') 
            label.setText(player.capitalize() + ': ' + status.capitalize())

def set_bet_box(self, reset:bool = False, deactive:bool = False):
    if reset:
        self.ui.groupbox_bet.setStyleSheet('')
        self.ui.label_stake_amount.setText('')
        print('Bet board reset!')
        return
    
    if deactive:
        self.ui.groupbox_bet.setStyleSheet('')
        self.ui.label_stake_amount.setText('$'+str(self.bets['seat1']))
        return

    if self.ui.label_stake_amount.text() == '': 
        self.func_bet_slider(1)
        
    self.ui.groupbox_bet.setStyleSheet(ss.ss_groupbox_bet_active)
    

def set_total(self, player=None):
    if player is None:
        for player in self.players:
            if player == 'dealer' and not self.dealer_close_card_shown:
                label = self.findChild(QLabel, f'label_{player}_total')
                open_card = self.hands[player][0]
                open_card_value = self.CARD_VALUES[open_card]
                label.setText(f"{open_card_value}")
            else: 
                total_label = self.findChild(QLabel, f'label_{player}_total')
                total = self.hand_values[player]
                total_label.setText(f"{total}")
    else:
        if player == 'dealer' and not self.dealer_close_card_shown:
            label = self.findChild(QLabel, f'label_{player}_total')
            open_card = self.hands[player][0]
            open_card_value = self.CARD_VALUES[open_card]
            label.setText(f"{open_card_value}")
        else: 
            total_label = self.findChild(QLabel, f'label_{player}_total')
            total = self.hand_values[player]
            total_label.setText(f"{total}")

def set_chips(self, reset:bool = False):
    if reset:
        for player in self.players:
            if player != 'dealer':
                for i in range(1,3):
                    label = self.findChild(QLabel, f'label_{player}_chips_image_{i}')
                    label.setPixmap(QPixmap(""))
    
        return
    for player in self.players:
        if player != 'dealer':
            chip_label_1 = self.findChild(QLabel, f'label_{player}_chips_image_1')
            chip_label_2 = self.findChild(QLabel, f'label_{player}_chips_image_2')
            if self.bets[player] <= 5:
                chip_label_1.setPixmap(QPixmap(f":/chips/chips{self.bets[player]}.png"))
                chip_label_2.setPixmap(QPixmap(""))
            else: 
                chip_label_1.setPixmap(QPixmap(":/chips/chips5.png"))
                chip_label_2.setPixmap(QPixmap(f":/chips/chips{self.bets[player] - 5}.png"))
    

def payout(self):
    for self.player, self.status in self.player_status.items():
        if self.player == 'dealer': 
            continue

        if self.status == 'win':
            bet = self.bets[self.player]
            profit = bet
            self.bankroll[self.player] += bet + profit

        elif self.status == 'blackjack':
            bet = self.bets[self.player]
            profit = bet * 3/2
            self.bankroll[self.player] += bet + profit
        
        elif self.status == 'push':
            bet = self.bets[self.player]
            self.bankroll[self.player] += bet 

        if self.status:
            try: 
                self.bankroll[self.player] = int(self.bankroll[self.player])
            except Exception:
                pass

            label = self.findChild(QLabel, f'label_{self.player}_budget_amount')
            label.setText("$"+str(self.bankroll[self.player]))

def check_game_over(self):
    for player, bankroll in self.bankroll.items():
        if bankroll == 0 and self.player_status[player] in ['bust', 'lose']:
            self.update_status(player, 'bankrupt')
            set_status_icon(self, player=player)
            label = self.findChild(QLabel, f'label_{player}_martini')
            label.setPixmap(QPixmap(""))
            return player

def set_seat(self, seat=None, reset:bool=False):
    if seat == "seat1":
        self.ui.frame_seat1.setStyleSheet(ss.ss_frame_seat1_activate)
        self.ui.frame_seat1_budget.setStyleSheet("")
        self.ui.frame_seat1_total.setStyleSheet("")
    elif seat == "seat2":
        self.ui.frame_seat2.setStyleSheet(ss.ss_frame_seat2_activate)
        self.ui.frame_seat2_budget.setStyleSheet("")
        self.ui.frame_seat2_total.setStyleSheet("")
    else: 
        if reset:
            self.ui.frame_seat1.setStyleSheet(ss.ss_frame_seat1_activate)
            self.ui.frame_seat1_budget.setStyleSheet(ss.ss_frame_seat_deactive)
            self.ui.frame_seat1_total.setStyleSheet(ss.ss_frame_seat_deactive)
            self.ui.frame_seat2.setStyleSheet(ss.ss_frame_seat2_activate)
            self.ui.frame_seat2_budget.setStyleSheet(ss.ss_frame_seat_deactive)  
            self.ui.frame_seat2_total.setStyleSheet(ss.ss_frame_seat_deactive)  


def set_agent_name(self, reset: bool = False, activate=True, seat='seat2'):
    if reset:
        self.ui.label_seat2_agent_name.setText("")
        return 

    # Eğer agent_name .pkl ile bitiyorsa, uzantıyı kaldır
    agent_name = self.agent_name
    if agent_name.endswith(".pkl"):
        agent_name = agent_name[:-4]  # Son 4 karakteri (.pkl) kaldır

    label_agent_name = self.findChild(QLabel, f"label_{seat}_agent_name")

    if label_agent_name:
        label_agent_name.setText(agent_name)
        if activate:
            label_agent_name.setStyleSheet(ss.ss_label_seat2_agent_name_active)
        else:
            label_agent_name.setStyleSheet(ss.ss_label_seat2_agent_name_deactive)

def update_console_list(self, state:str=None, action:str=None, exploration:bool=None, next_state:str=None, reward:str=None, Q:str=None, reset:bool = False):
    try:
        if reset:
            self.ui.listWidget_console.clear()
            return

        type = "🎲" if exploration else "🧠"

        color = QColor("#e1d8ec") if exploration else QColor("#ff6dc6")

        item_text = f"{state} --> {action} {type} --> {next_state} R: {reward}, Q: {round(Q, 1)}"

        new_item = QListWidgetItem(item_text)
        new_item.setForeground(color)

        # Remove sorting if enabled
        self.ui.listWidget_console.setSortingEnabled(False)

        # Insert the new item at the end of the list (standard behavior)
        self.ui.listWidget_console.addItem(new_item)
        if not self.ui.listWidget_console.hasFocus():
            self.ui.listWidget_console.scrollToBottom()


    except Exception as err:
        print("An Exception occurred in update_console_list:", err)
        traceback.print_exc()


def update_last_rounds_list(self, episode: int=None, result: str=None, loss_profit: float=None, double: bool=None, reset: bool = False):
    try:
        if reset:
            self.ui.listWidget_last_rounds.clear()
            return

        double_str = " D" if double else ""

        # Format loss_profit correctly (integer -> no decimal, float -> keep decimals)
        loss_profit = float(loss_profit)
        if loss_profit.is_integer():
            loss_profit_str = f"${int(loss_profit)}"
        else:
            loss_profit_str = f"${loss_profit}"

        # Define specific colors for different results
        color = QColor("#d44c3a") if result in ["bust", "lose", "bankrupt"] else QColor("#9ed43a") if result == "win" else QColor("#787c74")

        # Create item text
        item_text = f"Eps {episode}: {result} {loss_profit_str}{double_str}"

        new_item = QListWidgetItem(item_text)
        new_item.setForeground(color)

        # Remove sorting if enabled
        self.ui.listWidget_last_rounds.setSortingEnabled(False)

        # Insert the new item at the end of the list (standard behavior)
        self.ui.listWidget_last_rounds.addItem(new_item)

        # Ensure the latest entry is visible
        if not self.ui.listWidget_last_rounds.hasFocus():
            self.ui.listWidget_last_rounds.scrollToBottom()

    except Exception as err:
        print("An Exception occurred in update_last_rounds_list:", err)
        traceback.print_exc()

def format_train_timer(self):
    """Formats time in 'MM:SS' or 'H:MM:SS' style."""
    h, remainder = divmod(self.train_timer_elapsed_time, 3600)
    m, s = divmod(remainder, 60)

    if h > 0:
        return f"{h}:{m:02}:{s:02}"  # 'H:MM:SS' formatı
    return f"{m}:{s:02}"  # 'MM:SS' formatı

def train_option_usability(self, usability:bool=True):
    self.ui.lineEdit_agentfilename.setEnabled(usability)
    self.ui.button_start_training.setEnabled(usability)
    self.ui.radioButton_training_episode.setEnabled(usability)
    self.ui.spinBox_training_episode.setEnabled(usability)
    self.ui.radioButton_rounds_without_losing.setEnabled(usability)
    self.ui.spinBox_rounds_without_losing.setEnabled(usability)
    self.ui.radioButton_achieved_budget.setEnabled(usability)
    self.ui.spinBox_achieved_budget.setEnabled(usability)

def add_trained_agent_to_interface(self, agent_name):
    sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
    self.ui.frame_trained_agent_x = QFrame(self.ui.scrollArea_agent_list_WidgetContents)
    self.ui.frame_trained_agent_x.setObjectName(f"frame_trained_agent_{agent_name}")
    sizePolicy.setHeightForWidth(self.ui.frame_trained_agent_x.sizePolicy().hasHeightForWidth())
    self.ui.frame_trained_agent_x.setSizePolicy(sizePolicy)
    self.ui.frame_trained_agent_x.setMinimumSize(QSize(0, 40))
    self.ui.frame_trained_agent_x.setMaximumSize(QSize(16777215, 40))
    self.ui.frame_trained_agent_x.setFrameShape(QFrame.Shape.StyledPanel)
    self.ui.frame_trained_agent_x.setFrameShadow(QFrame.Shadow.Raised)
    self.ui.horizontalLayout_22 = QHBoxLayout(self.ui.frame_trained_agent_x)
    self.ui.horizontalLayout_22.setSpacing(10)
    self.ui.horizontalLayout_22.setObjectName("horizontalLayout_22")
    self.ui.horizontalLayout_22.setContentsMargins(10, 0, 5, 0)
    self.ui.button_trained_agent_x = QPushButton(self.ui.frame_trained_agent_x)
    self.ui.button_trained_agent_x.setObjectName(f"button_trained_agent_{agent_name}")
    sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
    sizePolicy4.setHorizontalStretch(0)
    sizePolicy4.setVerticalStretch(0)
    sizePolicy4.setHeightForWidth(self.ui.button_trained_agent_x.sizePolicy().hasHeightForWidth())
    self.ui.button_trained_agent_x.setSizePolicy(sizePolicy4)
    self.ui.button_trained_agent_x.setText(agent_name)
    self.ui.button_trained_agent_x.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    self.ui.button_trained_agent_x
    self.ui.horizontalLayout_22.addWidget(self.ui.button_trained_agent_x)
    self.ui.button_delete_trained_agent_x = QPushButton(self.ui.frame_trained_agent_x)
    self.ui.button_delete_trained_agent_x.setObjectName(f"button_delete_trained_agent_{agent_name}")
    self.ui.button_delete_trained_agent_x.setMinimumSize(QSize(24, 24))
    self.ui.button_delete_trained_agent_x.setMaximumSize(QSize(24, 24))
    self.ui.button_delete_trained_agent_x.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    self.ui.button_delete_trained_agent_x.setText("✖")
    self.ui.button_delete_trained_agent_x.setStyleSheet("""
        QPushButton{
            background: transparent;
            color: rgba(212, 76, 58,0.66);
            font: 16pt "Forte";
            border-radius: 12px;
        }
        QPushButton:hover{
            color: rgba(212, 76, 58, 1)                         
        }
    """)
    
    self.ui.horizontalLayout_22.addWidget(self.ui.button_delete_trained_agent_x)
    self.ui.horizontalLayout_agent_list.addWidget(self.ui.frame_trained_agent_x)


def menu_page(self):
    self.ui.stackedWidget_train_agent.setCurrentIndex(0)
    self.ui.stackedWidget_agent_game_selection.setCurrentIndex(0)
    self.ui.stackedwidget_content.setCurrentIndex(0)

def game_page(self, training_mode=False):
    self.ui.stackedwidget_content.setCurrentIndex(1)
    if training_mode:
        self.ui.stackedWidget_options.setCurrentIndex(1)
    else: 
        self.ui.stackedWidget_options.setCurrentIndex(0)
    

