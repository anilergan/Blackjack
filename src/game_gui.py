from PySide6.QtCore import QEventLoop, QTimer

# User Interface Libs (PyQt6)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from game_utils import (
    next_round_button_usability,
    move_buttons_usability,
    bet_frame_usabilty,
    set_budget,
    set_totalframe_and_status,
    display_cards,
    check_blackjack, 
    set_players_cocktail_and_smoke,
    announce,
    set_status_board,
    set_bet_box,
    set_move_box,
    set_total,
    set_chips,
    payout,
    menu_page,
    game_page,
)

# Game Dynamis
from game_dynamics import BlackjackDynamics
from qt.qt_blackjack import Ui_MainWindow


class BlackjackGUI(QMainWindow, BlackjackDynamics):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # SIGNAL-SLOTS ------------------------
        # Login Page Buttons
        self.ui.button_one_player_game.clicked.connect(
            lambda: self.func_button_one_player_game(True)
        )

        self.ui.button_exit.clicked.connect(self.func_button_exit)

        # Game Page Slots
        self.ui.button_hit.clicked.connect(lambda: self.func_hit())
        self.ui.button_stand.clicked.connect(lambda: self.func_stand())
        self.ui.button_double.clicked.connect(lambda: self.func_double())
        self.ui.button_next_round.clicked.connect(lambda: self.pipeline_init_next_round())
        self.ui.slider_bet.valueChanged.connect(self.func_bet_slider)

        # Game Page Menu
        self.ui.button_menu.clicked.connect(self.func_menu)
        self.ui.button_reset.clicked.connect(self.func_reset)

        menu_page(self)

    # SİGNAL-SLOTS Functions -------------------------------------

    # Menu Page Signal-Slots ---------------------------------
    def func_button_one_player_game(self, init: bool = False):
        self.game_mode = "OnePlayerGame"

        self.round = 0

        self.players = ["dealer", "seat1"]

        self.bankroll = {"seat1": 10}

        self.bets = {"seat1": 0}

        game_page(self)

        self.pipeline_init_next_round()

        check = self.pipeline_check_blackjack()

        if check:
            self.pipeline_end_round()



    # Game page Signal-Slots ---------------------------------
    def func_button_exit(self):
        QApplication.quit()

    def func_menu(self):
        self.pipeline_reset_game_page()
        menu_page(self)
        if self.timer:
            self.timer.stop()

    def func_reset(self):
        self.pipeline_reset_game_page()
        if self.timer:
            self.timer.stop()

        if self.game_mode == "OnePlayerGame":
            self.func_button_one_player_game()

    def func_hit(self, player="seat1"):
        if self.ui.button_hit.isEnabled():
            super().hit()
            display_cards(self)
            set_total(self)

            if self.hand_values["seat1"] > 21:
                set_totalframe_and_status(self)

                self.update_status(player=player, status="bust")

                # if opponent is bust as well or there is no opponent, round ends.
                if len(self.players) == 2 or self.player_status["seat2"] == "bust":
                    self.pipeline_end_round()

                # if opponent is not 'in play' too.
                elif self.player_status["seat2"] != "in play":
                    self.countdown = 1
                    self.init_timer(mode="dealer_turn")
                    self.pipeline_end_round()

                # so opponent is still in play
                elif self.player_status["seat2"] == "in play":
                    pass
            QApplication.processEvents()
        else:
            return

    def func_stand(self, player="seat1"):
        if self.ui.button_hit.isEnabled():
            move_buttons_usability(self, False)
            self.update_status(player=player, status="stand")

            set_totalframe_and_status(self)

            # if there is no player whose status 'in play' (exclude dealer)
            if list(self.player_status.values()).count("in play") == 1:
                self.countdown = 1
                self.init_timer(mode="dealer_turn")
                self.pipeline_end_round()

            # so opponent is still in play
            elif list(self.player_status.values()).count("in play") > 1:
                pass
        else:
            return

    def func_double(self, player="seat1"):
        if self.bankroll[player] >= self.bets[player]:
            self.bankroll[player] = self.bankroll[player] - self.bets[player]
            self.bets[player] *= 2
        else:
            return

        self.func_hit(player)
        self.func_stand(player)

    def func_bet_slider(self, value):
        if self.bankroll["seat1"] < 10:
            self.ui.slider_bet.setMaximum(self.bankroll["seat1"])

        else:
            self.ui.slider_bet.setMaximum(10)

        self.bets["seat1"] = value
        self.ui.label_stake_amount.setText(str(value))
        self.bets["seat1"] = value
        set_chips(self)

        budget = self.bankroll["seat1"] - self.bets["seat1"]

        self.ui.label_seat1_budget_amount.setText(str(budget))

    # Timer ---------------------------------

    def init_timer(self, mode):
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.handle_timeout(mode))
        self.event_loop = QEventLoop()
        self.timer.start(1000)
        self.event_loop.exec()

    def handle_timeout(self, mode):
        if mode == "init":
            # If user quit game page
            announce(self)

            if self.ui.stackedwidget_content.currentIndex() == 0:
                self.timer.stop()
                self.event_loop.quit()
                return

            if self.countdown == 3:
                bet_frame_usabilty(self, True)
                set_bet_box(self)


            elif self.countdown == 0:
                self.timer.stop()
                self.event_loop.quit()
                self.ui.label_cd.setText("")

        elif mode == "dealer_turn":
            if self.ui.stackedwidget_content.currentIndex() == 0:
                self.timer.stop()
                self.event_loop.quit()
                return

            self.dealer_turn()

        elif mode == "players_hit":
            if self.ui.stackedwidget_content.currentIndex() == 0:
                self.timer.stop()
                self.event_loop.quit()
                return

            self.opponent_turn()

        if mode != "init" and self.countdown == 1:
            self.countdown -= 1
        elif mode == "init":
            self.countdown -= 1

    # Dealer Plays ---------------------------------

    def dealer_turn(self):
        if self.close_card_shown:
            super().hit("dealer")
        self.close_card_shown = True

        display_cards(self)
        set_total(self)

        if self.hand_values["dealer"] < 17 and self.countdown == 0:
            self.countdown += 1

        elif self.countdown == 0:
            self.timer.stop()
            self.event_loop.quit()
            return

        elif self.hand_values["dealer"] >= 17 and self.hand_values["dealer"] <= 21:
            highest_hand = 0
            highest_hand_player = None

            for player, hand_value in self.hand_values.items():
                if hand_value > highest_hand and self.hand_values[player] <= 21:
                    highest_hand_player = player
                    highest_hand = hand_value

                elif hand_value == highest_hand:
                    self.player_status[highest_hand_player] = "push"
                    self.player_status[player] = "push"

        elif self.hand_values["dealer"] > 21:
            self.player_status["dealer"] = "bust"

    # Multiple Player Game Functions ------------------------

    def opponent_turn(self, player: str):
        if self.countdown == 0:
            self.timer.stop()
            self.event_loop.quit()
            return

        if player not in self.players_bust:
            super().hit(player)
            super().update_hand_values()
            display_cards(self)
            set_total(self)

            if self.hand_values[player] > 21:
                self.players_bust.add(player)
                set_totalframe_and_status(self)

    def opponent_bet(self):
        pass

    # PIPELINES ---------------------------------------
    def pipeline_end_round(self):
        announce(self, round_end=True)
        move_buttons_usability(self, False)
        set_status_board(self)
        set_totalframe_and_status(self)
        set_players_cocktail_and_smoke(self)
        payout(self)
        next_round_button_usability(self, True)

        QApplication.processEvents()

    def pipeline_init_next_round(self):
        move_buttons_usability(self, False)
        bet_frame_usabilty(self, False)
        next_round_button_usability(self, False)

        if not hasattr(self, "countdown"):
            print('There is no countdown yet, it is going to be the first time it will be defined as 5.')
            self.countdown = 5
        else:
            print('There is a countdown:', self.countdown)
        self.init_timer(mode='init')
        self.countdown = 3
        
        set_bet_box(self, deavtive=True)
        bet_frame_usabilty(self, False)
        set_move_box(self)
        move_buttons_usability(self,True)

        display_cards(self, reset=True)
        set_totalframe_and_status(self, reset=True)
        set_chips(self, reset=True)

        BlackjackDynamics.__init__(self)

        self.round += 1
        self.ui.label_round_number.setText(str(self.round))

        self.bankroll["seat1"] = self.bankroll["seat1"] - self.bets["seat1"]

        super().initialize_hands(self.players)

        display_cards(self)
        set_total(self)

        set_chips(self)

        for player in self.players:
            self.update_status(player=player, status="in play")

        QApplication.processEvents()

    def pipeline_check_blackjack(self):
        check_blackjack(self)

        # Blackjack hand exists
        if "blackjack" in self.player_status.values():
            # Figure out these seperetaly
            # If dealer blackjack
            # if players blackjack

            # Dealer has Blackjack hand
            if self.player_status["dealer"] == "blackjack":
                return True

            # If it's multiple player game, player takes but game go on.
            elif (
                list(self.player_status.values()).count("blackjack")
                < len(self.players) - 1
            ):
                return False

            # If it's one player game round ends, player takes.
            else:
                return True

        else:
            return False

        # Blackjack hand does not exists

        # Game go on

    def pipeline_reset_game_page(self):
        move_buttons_usability(self, False)
        bet_frame_usabilty(self, False)
        display_cards(self, reset=True)
        set_totalframe_and_status(self, reset=True)
        set_chips(self, reset=True)
        announce(self, reset=True)
        set_status_board(self, reset=True)
        set_bet_box(self, reset=True)
        set_move_box(self, reset=True)
        set_budget(self, reset=True)
