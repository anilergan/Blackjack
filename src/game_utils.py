from PySide6.QtGui import QPixmap

# User Interface Libs (PyQt6)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGroupBox,
    QLabel,
)

# Game Dynamis
import ss

def next_round_button_usability(self, usability:bool=True):
    self.ui.button_next_round.setEnabled(usability)
    if usability:
        self.ui.button_next_round.setStyleSheet(ss.ss_button_next_round_active)
    else: 
        self.ui.button_next_round.setStyleSheet(ss.ss_button_next_round_deactive)


def move_buttons_usability(self, usability:bool=True):
    self.ui.button_stand.setEnabled(usability)
    self.ui.button_hit.setEnabled(usability)
    
    if self.bets['seat1'] > self.bankroll['seat1']:
        self.ui.button_double.setEnabled(False)
    
    else:
        self.ui.button_double.setEnabled(usability)

def bet_frame_usabilty(self, usability:bool):
    self.ui.slider_bet.setEnabled(usability)

def set_budget(self, reset:bool = False):
    if reset:
        for player in self.players:
            if player != 'dealer':
                label = self.findChild(QLabel, f'label_{player}_budget_amount')
                label.setText('')
                label = self.findChild(QLabel, f'label_{player}_budget_dollar')
                label.setText('')

    for player in self.players:
        if player != 'dealer':
            label = self.findChild(QLabel, f'label_{player}_budget_amount')
            label.setText(str(self.bankroll[player] - self.bets[player]))

            label = self.findChild(QLabel, f'label_{player}_budget_dollar')
            label.setText('$')

def set_totalframe_and_status(self, reset:bool = False):

    if reset:
        for player in self.players:
            frame = self.findChild(QFrame, f'frame_{player}_total')
            label = self.findChild(QLabel, f'label_{player}_status')
            
            if label: label.setPixmap(QPixmap(""))
            if frame: frame.setStyleSheet('')

        return


    for player, status in self.player_status.items():
        if status:
            frame = self.findChild(QFrame, f'frame_{player}_total')
            label = self.findChild(QLabel, f'label_{player}_status')   

            if status == 'blackjack':
                icon = QPixmap(":/status/jack.png")
                frame.setStyleSheet(
                f"""
                #frame_{player}_total {{
                background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:0.1, stop:0 rgba(29,25,43,100), stop:0.75 transparent);
                border-radius: 10px;
                }}
                """
                )
            
            elif status == 'stand':
                icon = QPixmap(":/icons/lose.png")
                frame.setStyleSheet(
                f"""
                #frame_{player}_total {{
                background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:0.1, stop:0 rgba(255,255,255,100), stop:0.75 transparent);
                border-radius: 10px;
                }}
                """
                )

            elif status == 'win':
                icon = QPixmap(":/icons/win.png")
                frame.setStyleSheet(
                f"""
                #frame_{player}_total {{
                background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:0.1, stop:0 rgb(212,185,58,100), stop:0.75 transparent);
                border-radius: 10px;
                }}
                """
                )
            
            elif status == 'push':
                icon = QPixmap(":/icons/push.png")
                frame.setStyleSheet(
                f"""
                #frame_{player}_total {{
                background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:0.1, stop:0 rgb(43,148,242,100), stop:0.75 transparent);
                border-radius: 10px;
                }}
                """
                ) 
            
            elif status == 'bust':
                icon = QPixmap(":/icons/lose.png")
                frame.setStyleSheet(
                f"""
                #frame_{player}_total {{
                background-color:  qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:0.1, stop:0 rgba(29,25,43,100), stop:0.75 transparent);
                border-radius: 10px;
                }}
                """
                )
            
            elif status == 'double':
                icon = QPixmap(":/icons/lose.png")
                frame.setStyleSheet(
                f"""
                #frame_{player}_total {{
                background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:0.1, stop:0 rgba(166,42,53,100), stop:0.75 transparent);
                border-radius: 10px;
                }}
                """
                )
            
            else: continue
            
            print('status: ', status)
            try:
                label.setPixmap(QPixmap(icon))
            except UnboundLocalError: 
                raise UnboundLocalError('set_totalframe_and_status içerisinde icon tanımlanamadı')

def display_cards(self, reset:bool=False):
    if reset:
        for player in self.players:
            frame = self.findChild(QFrame, f'frame_{player}_cards')
            for label in frame.findChildren(QLabel):
                label.setPixmap(QPixmap())

            total_label = self.findChild(QLabel, f'label_{player}_total')
            total_label.setText('')


    for player in self.players:
        if player == 'dealer' and self.close_card_shown == False:
            for index, card in enumerate(self.hands[player]):
                if index == 0:
                    icon = QPixmap(f":/cards/{card}.png")
                    label = self.findChild(QLabel, f"label_{player}_card{index+1}")
                    if label: label.setPixmap(icon)
                elif index == 1:
                    icon = QPixmap(f":/cards/close_card.png")
                    label = self.findChild(QLabel, f"label_{player}_card{index+1}")
                    if label: label.setPixmap(icon)

        else:
            for index, card in enumerate(self.hands[player]):
                icon = QPixmap(f":/cards/{card}.png")
                label = self.findChild(QLabel, f"label_{player}_card{index+1}")
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
        if player == 'dealer': 
            continue

        if reset or status == 'push':
            martini = self.findChild(QLabel, f'label_{player}_martini')
            martini.setPixmap(QPixmap(""))
        
        elif status == 'win' or 'blackjack':
            martini = self.findChild(QLabel, f'label_{player}_martini')
            martini.setPixmap(QPixmap(":/alcohol/cokctail.png"))
        
        elif status == 'bust':
            martini = self.findChild(QLabel, f'label_{player}_martini')
            martini.setPixmap(QPixmap(":/alcohol/smoke.png"))           
    
def announce(self, reset:bool = False, round_end:bool = False):
    if reset:
        self.ui.label_announce.setText("")
        self.ui.label_cd.setText("")
        return
    
    if round_end:
        self.ui.label_announce.setText(f"Round {self.round} ends!")
        self.ui.label_cd.setText("")
        return
    
    self.ui.label_cd.setText(str(self.countdown))
    
    if self.countdown > 3:
        self.ui.label_announce.setText('Welcome! Take your place.')

    elif self.countdown <= 3 and self.countdown > 0:
        self.ui.label_announce.setText('Bets are open.')
        print('self.player_status:\n', self.player_status)
        
    
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
            label = self.findChild(QLabel, f'label_status_{player}') 
            label.setText(status.capitalize())

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
    QApplication.processEvents()


def set_total(self, include_close_card:bool=False):
    for player in self.players:
        if player == 'dealer' and len(self.hands['dealer']) == 2 and not include_close_card:
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

def payout(self):
    for self.player, self.status in self.player_status.items():
        if self.player == 'dealer': 
            continue

        if self.status == 'win':
            # $10 -> $10 + initial
            profit = self.bets[self.player] + self.bets[self.player]
            self.bankroll[self.player] = profit

        
        elif self.status == 'blackjack':
            # $10 -> $15 + initial
            profit = self.bets[self.player] * 3/2 + self.bets[self.player]
            self.bankroll[self.player] = profit
        
        elif self.status == 'push':
            # initial
            profit = self.bets[self.player]
            self.bankroll[self.player] = profit

        if self.status:
            label = self.findChild(QLabel, f'label_{self.player}_budget_amount')
            label.setText(str(self.bankroll[self.player]))

def menu_page(self):
    self.ui.stackedwidget_content.setCurrentIndex(0)

def game_page(self):
    self.ui.stackedwidget_content.setCurrentIndex(1)