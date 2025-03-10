import traceback
import pickle
import os
from random import choice

from PySide6.QtCore import QEventLoop, QTimer
from PySide6.QtGui import QIcon

# User Interface Libs (PyQt6)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QMessageBox,
    QSpacerItem,
    QPushButton,
    QWidget,
    QSizePolicy,
    QFrame,
    QTableWidget,
    QTableWidgetItem,
    QComboBox,
)

from agent.SimpleDecisionMakingAgent import SimpleDecisionMakingAgent as SDMA
from agent.QAgent import QAgent
# Game Dynamis
from game_utils import (
    announce,
    bet_frame_usabilty,
    check_blackjack,
    check_game_over,
    display_cards,
    format_train_timer,
    game_page,
    grad_condition_spinbox_color,
    menu_page,
    move_buttons_usability,
    next_round_button_usability,
    payout,
    set_agent_name,
    set_bet_box,
    set_budget,
    set_chips,
    set_cocktail_and_smoke,
    set_seat,
    set_status_board,
    set_status_icon,
    set_total,
    update_console_list,
    update_last_rounds_list,
    train_option_usability,
    add_trained_agent_to_interface,
)
from qt.qt_blackjack import Ui_MainWindow
from ss import ss_frame_seat2_activate, ss_frame_seat_deactive, ss_label_training_console, ss_listWidget_console


class BlackjackGUI(QMainWindow):
    number_cards = ('2','3','4','5','6','7','8','9','10')
    face_cards = ('K', 'Q', 'J', 'A')
    DECK = number_cards + face_cards
    CARD_VALUES = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'K': 10,
            'Q': 10,
            'J': 10, 
            'A': 11,
        }
    TRAINED_AGENT_PATH = "src\\agent\\trained_agents"
    
    hand_value_before = None

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Blackjack by Anıl Ergan")

        # SIGNAL-SLOTS ------------------------
        # Menu Page Buttons
        self.ui.button_train_agent.clicked.connect(self.train_agent)
        self.ui.button_train_agent_list.clicked.connect(self.func_train_agent_list)
        self.ui.button_train_agent_list_back.clicked.connect(self.func_train_agent_list_back)
        self.ui.button_one_player_game.clicked.connect(self.one_player_game)
        self.ui.button_single_agent.clicked.connect(self.func_button_single_agent)
        self.ui.comboBox_single_agent_1.currentIndexChanged.connect(self.func_info)
        self.ui.comboBox_multiple_agent_1.currentIndexChanged.connect(self.func_info)
        self.ui.comboBox_multiple_agent_2.currentIndexChanged.connect(self.func_info)
        self.ui.button_multiple_agent.clicked.connect(self.func_button_multiple_agent)

        self.ui.button_single_agent_back.clicked.connect(lambda: self.func_button_back(True))
        self.ui.button_multiple_agent_back.clicked.connect(lambda: self.func_button_back(True))
        self.ui.button_info_sdma_back.clicked.connect(lambda: self.func_button_back(False))

        self.ui.button_single_agent_play.clicked.connect(self.single_agent_game)
        self.ui.button_multiple_agent_play.clicked.connect(self.multiple_agent_game)

        self.ui.button_agent_info_back.clicked.connect(lambda: self.func_button_back(True))
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

        # Training Page Slots
        self.ui.button_start_training.clicked.connect(self.func_start_training)
        self.ui.button_save_and_quit_training.clicked.connect(self.func_menu)
        self.ui.button_quit_training.clicked.connect(self.func_menu)

        menu_page(self)
        self.ui.stackedWidget_menu.setCurrentIndex(0)
        set_seat(self, reset=True)

        # ------- Customize in Code ------- 
        self.ui.radioButton_training_episode.toggled.connect(lambda checked: grad_condition_spinbox_color(checked, self, "spinBox_training_episode"))
        self.ui.radioButton_rounds_without_losing.toggled.connect(lambda checked: grad_condition_spinbox_color(checked, self, "spinBox_rounds_without_losing"))
        self.ui.radioButton_achieved_budget.toggled.connect(lambda checked: grad_condition_spinbox_color(checked, self, "spinBox_achieved_budget"))

    # ------- Customize in Code -------
       

    # -------------- Game Mobility Functions --------------

    def update_hand_values(self):
        for player, hand in self.hands.items():
            ace_num = hand.count('A')
            total = 0
            for card in hand:
                total += self.CARD_VALUES[card]
                if total > 21 and ace_num != 0:
                    total -= 10
                    ace_num -= 1
            self.hand_values[player] = total
    
    def update_status(self, player:str, status:str):
        possible_status = ['in play', 'blackjack', 'stand', 'win', 'push', 'bust', 'double', 'lose', 'bankrupt']
        if status not in possible_status:
            raise Exception('Status could not be updated: VALID STATUS.')
        
        if player not in self.players:
            raise Exception('Status could not be updated: VALID PLAYER')
        
        self.player_status[player] = status
               
    def initialize_hands(self, players):
        for player in players:
            self.hands[player] = []
            # Kurpiyer kendine 2 kart çeker. 
            card = choice(self.DECK)
            self.hands[player].append(card)
            card = choice(self.DECK)
            self.hands[player].append(card)
        # self.hands['dealer'] = ['2', '5']
        # self.hands['seat1'] = ['Q', 'A']
        # self.hands['seat2'] = ['5', '8']
        self.update_hand_values()
    
    def hit(self, player = 'seat1'):
        card = choice(self.DECK)
        self.hands[player].append(card)
        if self.game_mode == "TrainAgent":
            self.hand_value_before = self.hand_values['seat2']
        self.update_hand_values()

    # ------------------- SİGNAL-SLOTS  -------------------
    # Menu Page Signal-Slots ------------------------------
    def one_player_game(self):
        self.game_mode = "OnePlayerGame"
        self.round = 0
        set_seat(self, "seat1")
        
        game_page(self)
        self.pipeline_init_next_round()
        if not hasattr(self, "timer"):
            return

    def func_button_single_agent(self):
        self.game_mode = 'SingleAgent'
        self.agent_name = None

        # Get the current items in the combo box
        existing_items = {self.ui.comboBox_single_agent_1.itemText(i) for i in range(self.ui.comboBox_single_agent_1.count())}

        # List trained agents from the directory
        trained_agents = [f for f in os.listdir(self.TRAINED_AGENT_PATH) if f.endswith(".pkl")]

        for agent_name in trained_agents:
            # Remove ".pkl" extension
            agent_name = agent_name[:-4]  # Remove last 4 characters (".pkl")

            # Only add if it does not already exist in the combo box
            if agent_name not in existing_items:
                self.ui.comboBox_single_agent_1.addItem(agent_name)

        self.ui.stackedWidget_agent_game_selection.setCurrentIndex(1)


    def func_button_multiple_agent(self):
        self.game_mode = 'MultipleAgent'
        self.agent_names = {
            'agent1_name': None,
            'agent2_name': None
        }
        trained_agents = [f for f in os.listdir(self.TRAINED_AGENT_PATH) if f.endswith(".pkl")]
        for agent_name in trained_agents:
            self.ui.comboBox_multiple_agent_1.addItem(agent_name)
            self.ui.comboBox_multiple_agent_2.addItem(agent_name)
        self.ui.stackedWidget_agent_game_selection.setCurrentIndex(2)

    def func_button_back(self, reset:bool):
        if reset:
            self.ui.comboBox_single_agent_1.setCurrentIndex(-1)
            self.ui.comboBox_multiple_agent_1.setCurrentIndex(-1)
            self.ui.comboBox_multiple_agent_2.setCurrentIndex(-1)
            self.ui.stackedWidget_menu.setCurrentIndex(0)
            self.ui.stackedWidget_agent_game_selection.setCurrentIndex(0)

        else:
            if self.game_mode == 'SingleAgent':
                self.ui.stackedWidget_agent_game_selection.setCurrentIndex(1)
            else:
                self.ui.stackedWidget_agent_game_selection.setCurrentIndex(2)
        
        QApplication.processEvents()

    def func_info(self):
        sender = self.sender()
        self.agent_name = sender.currentText()
        if self.agent_name == "Simple Decision-Making Agent":
            self.ui.stackedWidget_agent_game_selection.setCurrentIndex(3)
        
        if self.game_mode == 'MultipleAgent':
            if sender.objectName == "comboBox_multiple_agent_1":
                self.agent_names['agent1_name'] = self.agent_name
            else: 
                self.agent_names['agent2_name'] = self.agent_name
        
    def single_agent_game(self):
        if self.agent_name is None:
            return
        elif self.agent_name == 'Simple Decision-Making Agent':
            self.agent = SDMA()
        else:
            try:
                # Dynamically create an instance of the class with the given name
                AgentClass = globals().get(self.agent_name[:-3])  # Look for class in global scope
                if AgentClass and callable(AgentClass):  # Ensure it's a valid class
                    self.agent = AgentClass()  # Instantiate the class
                    for key, value in self.agent.data.items():
                        if hasattr(self.agent, key):  # Ensure that the attribute exists in the class
                            setattr(self.agent, key, value) 
                    print('self.agent_name:', self.agent_name)
                    file_name = f"{self.agent_name}.pkl"  # Format index as '001', '002', etc.
                    self.agent_file_path = os.path.join(self.TRAINED_AGENT_PATH, file_name)
                    self.agent.load_trained_agent(self.agent_file_path)
                else:
                    raise ValueError(f"Agent class '{self.agent_name}' not found.")
            except Exception as e:
                print(f"Error: {e}")


        self.game_mode = "SingleAgentGame"
        self.round = 0
        set_seat(self, "seat1")
        set_seat(self, "seat2")
        set_agent_name(self, activate=False)

        game_page(self)

        self.pipeline_init_next_round()
        if not hasattr(self, "timer"):
            return

    def multiple_agent_game(self, agent_names):
        if not any(agent_name is None for agent_name in agent_names.values()):
            print('Multiple Agent Game will start!')
        else:
            print('Select agents first!')
              
    def train_agent(self):
        set_seat(self, "seat2")
        self.game_mode = "TrainAgent"
        self.ui.label_announce.setText("Agent Training Simulation")
        self.ui.frame_seat1.setStyleSheet(ss_frame_seat_deactive)
        self.ui.frame_seat2.setStyleSheet(ss_frame_seat2_activate)
        self.ui.stackedWidget_options.setCurrentIndex(1)
        self.ui.label_training_console.setStyleSheet(ss_label_training_console)
        self.ui.listWidget_console.setStyleSheet(ss_listWidget_console)
        train_option_usability(self, True)

        self.ui.stackedwidget_content.setCurrentIndex(1)

    def func_start_training(self):
        start_training_error_msg = QMessageBox()
        start_training_error_msg.setIcon(QMessageBox.Warning)
        start_training_error_msg.setWindowTitle("Warning")
        start_training_error_msg.setWindowIcon(QIcon(":/icons/game.png"))
        
        self.agent_file_name = self.ui.lineEdit_agentfilename.text()
        if not self.agent_file_name.strip():
            start_training_error_msg.setText("Agent Name can not be empty.")
            start_training_error_msg.exec_()
            return

        index = 1  # Start at 001
        while True:
            file_name = f"{self.agent_file_name}{index:03d}.pkl"  # Format index as '001', '002', etc.
            self.agent_file_path = os.path.join(self.TRAINED_AGENT_PATH, file_name)
            
            if not os.path.exists(self.agent_file_path):  # If file does not exist, pick this name
                self.agent_name = file_name  # Assign the available name
                break  # Stop searching
            index += 1  # Move to the next number

        print("Assigned agent name:", self.agent_name)

        if self.agent_file_name in globals() and isinstance(globals()[self.agent_file_name], type):
            self.agent = globals()[self.agent_file_name]()
            print("self.agent is described!")
        else: 
            start_training_error_msg.setText(f"Training could not be started: The class '{self.agent_file_name}' is not found. Please be sure the agent name is right and the class is imported on game_gui.py")
            start_training_error_msg.exec_()
            return
        
        
        self.gradiuation_conditions = {
            "Training Episodes": None, #Default
            "Rounds Without Losing": None, #None
            "Achieved Budget": None, #None
        }

        if self.ui.radioButton_training_episode.isChecked():
            self.gradiuation_conditions['Training Episodes'] = int(self.ui.spinBox_training_episode.text())
        if self.ui.radioButton_rounds_without_losing.isChecked():
            self.gradiuation_conditions['Rounds Without Losing'] = int(self.ui.spinBox_rounds_without_losing.text())
        if self.ui.radioButton_achieved_budget.isChecked():
            self.gradiuation_conditions['Achieved Budget'] = int(self.ui.spinBox_achieved_budget.text())
        
        set_seat(self, "seat2")
        set_agent_name(self, activate=False)
        train_option_usability(self, False)
        self.ui.button_save_and_quit_training.setEnabled(True)

        self.game_count = 1
        
        self.total_episode = 1
        self.round_without_lose = 0
        self.max_achieved_budget = 10

        self.ui.label_stats_exploration_rate.setText(f"Exploration Rate: {round(self.agent.epsilon,2)}")
        self.ui.label_stats_game_count.setText(f"Game Count: {self.game_count}")
        self.ui.label_stats_episode.setText(f"Total Episode (Round): {self.total_episode}")
        self.ui.label_stats_mab.setText(f"Max Achieved Budget: {self.max_achieved_budget}")

        self.ui.label_announce.setText("Train has started! Agent is learning...")

        self.train_timer = QTimer(self)
        self.train_timer.timeout.connect(self.update_train_timer)
        self.train_timer_elapsed_time = 0
        self.train_timer.start(1000)
        self.train_timer_text = ""

        self.round = 0
        self.train_loop_wrapper()

    def train_loop_wrapper(self):
        training_done = self.train_loop()
        if not training_done and hasattr(self, "train_timer"):
            try:
                self.countdown = 1 if self.ui.radioButton_training_speed_1.isChecked() else (0.5 if self.ui.radioButton_training_speed_05.isChecked() else 0.1)
                QTimer.singleShot(int(self.countdown*1000), self.train_loop_wrapper)
            except Exception as exp:
                print('an exception occured on train_loop_wrapper:', exp)
                return 
        elif hasattr(self, "train_timer"):
            try:
                if self.train_timer:
                    self.train_timer.stop()
                    self.event_loop.quit()
                    del self.train_timer 
            except Exception:
                pass

            self.ui.label_announce.setText(f"{self.agent_name[:-4]} training is done.")

            print('Training is done.')
            self.ui.button_save_and_quit_training.setEnabled(False)
            try:
                self.agent.save_trained_agent(
                    path = self.agent_file_path
                )
            except Exception as err:
                print('Trained agent could not be saved, an error occured:', err)
            
            else:
                print('Agent is saved sucessfully!')

    def train_loop(self):
        try:
            self.ui.label_stats_episode.setText(f"Total Episode (Round): {self.total_episode}")
            self.pipeline_init_next_round()
            
            self.countdown = 1 if self.ui.radioButton_training_speed_1.isChecked() else (0.5 if self.ui.radioButton_training_speed_05.isChecked() else 0.1)
            self.bankroll_before = self.bankroll['seat2']

            self.init_timer(mode="seat2 turn")
            self.bankroll_after = self.bankroll['seat2']
            if self.ui.stackedwidget_content.currentIndex() == 0:
                return
            
            self.ui.label_stats_exploration_rate.setText(f"Exploration Rate: {round(self.agent.epsilon,2)}")

            if self.player_status["seat2"] == "bankrupt" or not self.bankroll['seat2']:
                self.game_count += 1
                self.ui.label_stats_game_count.setText(f"Game Count: {self.game_count}")
                self.round = 0
            else:
                self.round += 1

            
            self.max_achieved_budget = max(self.max_achieved_budget, self.bankroll['seat2'])
            self.ui.label_stats_mab.setText(f"Max Achieved Budget: {self.max_achieved_budget}")

            if self.player_status['seat2'] not in ['lose', 'bust']:
                self.round_without_lose += 1
            else:
                self.round_without_lose = 0
            
            update_last_rounds_list(
                self,
                episode = self.total_episode,
                result = self.player_status['seat2'],
                loss_profit = self.bankroll_after - self.bankroll_before,
                double = True if self.action_move == "double" else False,
            )

            self.total_episode += 1
            QApplication.processEvents()

            if self.gradiuation_conditions['Training Episodes'] and self.gradiuation_conditions["Training Episodes"] == self.total_episode:
                return True
            elif self.gradiuation_conditions['Rounds Without Losing'] and self.gradiuation_conditions['Rounds Without Losing'] == self.round_without_lose:
                return True
            elif self.gradiuation_conditions['Achieved Budget'] and self.gradiuation_conditions['Achieved Budget'] <= self.max_achieved_budget:
                return True

        except Exception as exception:
            print('An exception occured on train_loop:', exception)
            traceback.print_exc()
            return
            
    def update_train_timer(self):
        self.train_timer_elapsed_time += 1
        self.train_timer_text = format_train_timer(self)
        announce(self)

    def func_train_agent_list(self):
        trained_agents = [f for f in os.listdir(self.TRAINED_AGENT_PATH) if f.endswith(".pkl")]
        self.update_trained_agent_list_interface(trained_agents)
        self.ui.stackedWidget_train_agent.setCurrentIndex(1)
    
    def func_train_agent_list_back(self):
        self.ui.stackedWidget_train_agent.setCurrentIndex(0)
    
    def update_trained_agent_list_interface(self, trained_agents:list):
        scroll_area_widget = self.findChild(QWidget, "scrollArea_agent_list_WidgetContents")

        if scroll_area_widget is not None:
            layout = scroll_area_widget.layout()

            if layout is not None:
                # Layout içindeki tüm öğeleri kontrol et (ters sırayla taramak önemli)
                for i in reversed(range(layout.count())):
                    item = layout.itemAt(i)

                    # Eğer öğe bir SpacerItem ise kaldır
                    if isinstance(item, QSpacerItem):
                        layout.removeItem(item)
                        del item  # Bellekten temizleme

                    # Eğer öğe bir QWidget (QFrame vb.) ise kaldır ve sil
                    elif item.widget() is not None:
                        widget = item.widget()
                        layout.removeWidget(widget)
                        widget.deleteLater()  # QWidget'i yok etmek için

        for agent_name in trained_agents:
            agent_name = agent_name[:-4]
            add_trained_agent_to_interface(self, agent_name)
            
            agent_button = self.findChild(QPushButton, f"button_trained_agent_{agent_name}")
            agent_button.clicked.connect(lambda _, name=agent_name: self.agent_information(name))

            delete_button = self.findChild(QPushButton, f"button_delete_trained_agent_{agent_name}")
            delete_button.clicked.connect(lambda _, name=agent_name: self.delete_agent_from_list(name))

        self.ui.horizontalSpacer_agent_list = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.ui.horizontalLayout_agent_list.addItem(self.ui.horizontalSpacer_agent_list)

    def delete_agent_from_list(self, agent_name):
        scroll_area_widget = self.findChild(QWidget, "scrollArea_agent_list_WidgetContents")
        frame_name = f"frame_trained_agent_{agent_name}"

        if scroll_area_widget is not None:
            layout = scroll_area_widget.layout()

            if layout is not None:
                frame = self.findChild(QFrame, frame_name)

                if frame is not None:
                    frame_layout = frame.layout()
                    if frame_layout is not None:
                        while frame_layout.count():
                            item = frame_layout.takeAt(0)
                            if item.widget():
                                item.widget().deleteLater()  
                            elif item.spacerItem():
                                del item  

                    layout.removeWidget(frame)
                    frame.deleteLater()
        
        # ✅ Check and delete the corresponding .pkl file
        if hasattr(self, "TRAINED_AGENT_PATH"):  # Ensure the attribute exists
            agent_file = os.path.join(self.TRAINED_AGENT_PATH, f"{agent_name}.pkl")
            if os.path.exists(agent_file):
                try:
                    os.remove(agent_file)
                    print(f"Deleted: {agent_file}")
                except Exception as e:
                    print(f"Error deleting {agent_file}: {e}")
        
        # ✅ Remove agent_name from comboBoxes
        combo_boxes = ["comboBox_single_agent_1", "comboBox_multiple_agent_1", "comboBox_multiple_agent_2"]
        
        for combo_name in combo_boxes:
            combo_box = self.findChild(QComboBox, combo_name)
            if combo_box is not None:
                index = combo_box.findText(agent_name)
                if index != -1:
                    combo_box.removeItem(index)


    def agent_information(self, agent_name):
        self.ui.label_agent_info_text.setText(f"{agent_name} Information")
        self.ui.tableWidget_qtablebet.clear()
        self.ui.tableWidget_qtablemove.clear()

        file_name = f"{agent_name}.pkl"
        agent_file_path = os.path.join(self.TRAINED_AGENT_PATH, file_name)
        try:
            with open(agent_file_path, "rb") as f:
                agent_data = pickle.load(f)
        except Exception as e:
            print('An error occured while reading agent data from path:', agent_file_path, 'Error:', e)
        
        # Load each Q-table separately
        self.load_q_table_in_interface(self.ui.tableWidget_qtablebet, agent_data["q_table_bet"])
        self.load_q_table_in_interface(self.ui.tableWidget_qtablemove, agent_data["q_table_move"])

        self.ui.tableWidget_qtablebet.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.tableWidget_qtablemove.setEditTriggers(QTableWidget.NoEditTriggers)

        self.ui.stackedWidget_menu.setCurrentIndex(1)

    def load_q_table_in_interface(self, table_widget, q_table):
        """Load a Q-table into the specified QTableWidget."""
        table_widget.setRowCount(0)  # Clear the existing table
        table_widget.setColumnCount(3)  # Three columns: State, Action, Q-Value
        table_widget.setHorizontalHeaderLabels(["State", "Action", "Q-Value"])

        row = 0
        for state, actions in q_table.items():  # Iterate over states
            for action, q_value in actions.items():  # Iterate over actions
                table_widget.insertRow(row)
                table_widget.setItem(row, 0, QTableWidgetItem(str(state)))  # State
                table_widget.setItem(row, 1, QTableWidgetItem(str(action)))  # Action
                table_widget.setItem(row, 2, QTableWidgetItem(f"{q_value:.4f}"))  # Q-value
                row += 1


    # Game page Signal-Slots ---------------------------------
    def func_button_exit(self):
        QApplication.quit()

    def func_menu(self):
        # Get the sender (the button that triggered this function)
        sender_button = self.sender()
        sender_name = sender_button.objectName() if sender_button else "Unknown"

        if sender_name == "button_save_and_quit_training":
            self.agent.save_trained_agent(
                path = self.agent_file_path
            )
        try:
            if self.timer:
                self.timer.stop()
                self.event_loop.quit()
                del self.timer
        except Exception:
            pass
        try: 
            if self.train_timer:
                self.train_timer.stop()
                self.event_loop.quit()
                del self.train_timer
        except Exception:
            pass

        try:
            if hasattr(self, "countdown"): 
                del self.countdown 
        except Exception:
            pass

        self.pipeline_reset_game_page()
        self.ui.label_training_console.setStyleSheet("color: transparent")
        self.ui.listWidget_console.setStyleSheet("")
        menu_page(self)


    def func_reset(self):
        self.pipeline_reset_game_page()
        try:
            if self.timer:
                self.timer.stop()
                self.event_loop.quit()
                del self.timer  
        except Exception:
            pass
        try:
            if hasattr(self, "countdown"):  
                del self.countdown  
        except Exception:
            pass

        if self.game_mode == "OnePlayerGame":
            self.one_player_game()

        if self.game_mode == "SingleAgentGame":
            self.single_agent_game()
        
        
    def func_hit(self, player="seat1"):
        if self.ui.button_hit.isEnabled() or player == 'seat2':
            self.hit(player)
            display_cards(self, player=player)
            set_total(self, player)

            if self.hand_values[player] > 21:
                self.update_status(player=player, status="bust")
                set_status_board(self, player=player)
                set_status_icon(self, player=player)

                if self.game_mode == 'OnePlayerGame' or (self.game_mode != 'TrainAgent' and player == 'seat2'):
                    if self.player_status['seat1'] not in ['stand', 'double']:
                        self.update_status('dealer', 'win')  
                    else:
                        if self.game_mode != "TrainAgent":
                            self.countdown = 1
                        else:
                            self.countdown = 1 if self.ui.radioButton_training_speed_1.isChecked() else (0.5 if self.ui.radioButton_training_speed_05.isChecked() else 0.1)
                        if player == 'seat2' and self.timer.isActive():
                            self.timer.stop()
                            self.event_loop.quit()
                            del self.timer 
                        self.init_timer(mode="dealer turn")
                        if self.timer.isActive():
                            self.timer.stop()
                            self.event_loop.quit()
                            del self.timer 
                        if self.ui.stackedwidget_content.currentIndex() == 0:
                            return                  

                elif self.game_mode == 'SingleAgentGame' and player == 'seat1':

                    move_buttons_usability(self, False)
                    if self.player_status['seat2'] == 'in play':
                        self.countdown = 1
                        self.init_timer(mode="seat2 turn")
                        try:
                            if self.timer.isActive():
                                self.timer.stop()
                                self.event_loop.quit()
                                del self.timer
                        except Exception: 
                            pass
                        if self.ui.stackedwidget_content.currentIndex() == 0:
                            return
                    if self.game_mode != "TrainAgent":
                        self.countdown = 1
                    else:
                        self.countdown = 1 if self.ui.radioButton_training_speed_1.isChecked() else (0.5 if self.ui.radioButton_training_speed_05.isChecked() else 0.1)
                    self.init_timer(mode="dealer turn")
                    if self.timer.isActive():
                        self.timer.stop()
                        self.event_loop.quit()
                        del self.timer  
                    if self.ui.stackedwidget_content.currentIndex() == 0:
                        return
                self.pipeline_end_round()
            QApplication.processEvents()
        
    def func_stand(self, player="seat1"):
        if self.ui.button_hit.isEnabled() or player == 'seat2':
            move_buttons_usability(self, False)
            if not self.player_status[player] == "double":
                self.update_status(player=player, status="stand")
            set_status_board(self, player=player)
            set_status_icon(self, player=player)
            
            if self.game_mode == "SingleAgentGame" and player == "seat1" and self.player_status['seat2'] != "blackjack":
                self.countdown = 1
                self.init_timer(mode="seat2 turn")
                try:
                    if self.timer.isActive():
                        self.timer.stop()
                        self.event_loop.quit()
                        del self.timer
                except Exception: 
                    pass
                if self.ui.stackedwidget_content.currentIndex() == 0:
                    return

            elif self.game_mode == "OnePlayerGame" or player == "seat2" or (self.game_mode == "SingleAgentGame" and self.player_status['seat2'] == "blackjack" and player == 'seat1'):
                if player == 'seat2':
                    try:
                        self.timer.stop()
                        self.event_loop.quit()
                        del self.timer
                    except Exception: 
                        pass
                if self.game_mode != "TrainAgent":
                    self.countdown = 1
                else:
                    self.countdown = 1 if self.ui.radioButton_training_speed_1.isChecked() else (0.5 if self.ui.radioButton_training_speed_05.isChecked() else 0.1)
                self.init_timer(mode="dealer turn")
                try:
                    self.timer.stop()
                    self.event_loop.quit()
                    del self.timer
                except Exception:
                    pass
                if self.ui.stackedwidget_content.currentIndex() == 0:
                    return
                self.pipeline_end_round() 
            
        
    def func_double(self, player="seat1"):
        if self.bankroll[player] >= self.bets[player]:
            self.bankroll[player] -= self.bets[player]
            self.bets[player] *= 2
            self.update_status(player, "double")
            set_budget(self)
            set_chips(self)
            QApplication.processEvents()
        else:
            return
        self.func_hit(player)
        if self.player_status[player] != "bust":
            self.func_stand(player)


    def func_bet_slider(self, value):
        if self.bankroll["seat1"] < 10:
            self.ui.slider_bet.setMaximum(self.bankroll["seat1"])

        else:
            self.ui.slider_bet.setMaximum(10)

        self.bets["seat1"] = value
        self.ui.label_stake_amount.setText('$'+str(value))

        set_chips(self)

        budget = self.bankroll["seat1"] - self.bets["seat1"]

        self.ui.label_seat1_budget_amount.setText("$"+str(budget))

    # Timer ---------------------------------

    def init_timer(self, mode):
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.handle_timeout(mode))
        self.event_loop = QEventLoop()
        if self.countdown >= 1:
            self.timer.start(1000)
        else:
            self.timer.start(self.countdown*1000)
        self.event_loop.exec()

    def handle_timeout(self, mode):
        if mode == "init":
            # If user quit game page

            announce(self)
            if self.game_mode == "TrainAgent" and self.countdown != 0:
                self.seat2_turn()

            elif self.countdown == 3:
                if self.game_mode == "SingleAgentGame":
                    self.seat2_turn()
                    
                elif self.game_mode == "MultiAgentGame":
                    self.seat1_turn()
                    self.seat2_turn()
                    return
                
                bet_frame_usabilty(self, True)
                display_cards(self, player='dealer')

            elif self.countdown == 0:
                self.timer.stop()
                self.event_loop.quit()
                self.ui.label_cd.setText("")

        elif mode == "dealer turn":
            self.dealer_turn()
            
        elif mode == "seat2 turn":
            self.seat2_turn()

        if self.ui.stackedwidget_content.currentIndex() == 0:
            return
        
        try:
            if mode != "init" and self.countdown <= 1:
                self.countdown -= self.countdown
            elif mode == "init" and self.countdown <= 1:
                self.countdown -= self.countdown
            elif mode == "init" and self.countdown > 1:
                self.countdown -= 1
        except Exception:
            return

    # Dealer Plays ---------------------------------

    def dealer_turn(self):
        if all([status in ['blackjack', 'bust'] for player, status in self.player_status.items() if player != 'dealer']) or self.ui.button_next_round.isEnabled():
            self.timer.stop()
            self.event_loop.quit()
            return 
        
        if self.dealer_close_card_shown:
            self.hit("dealer")
        else:
            self.dealer_close_card_shown = True

        display_cards(self, player='dealer')
        set_total(self)

        if self.hand_values["dealer"] < 17 and self.countdown == 0:
            self.countdown += 1

        elif self.hand_values["dealer"] >= 17 and self.hand_values["dealer"] <= 21:
            for player, hand_value in self.hand_values.items():
                if player == 'dealer': 
                    self.update_status('dealer', 'stand')
                elif self.player_status[player] in ["stand", "double"]:
                    if hand_value > self.hand_values["dealer"] :
                        self.update_status(player, 'win')
                    elif hand_value == self.hand_values["dealer"]:
                        self.update_status(player, 'push')
                        self.update_status('dealer', 'push')
                    elif hand_value < self.hand_values["dealer"]:
                        self.update_status(player, 'lose')

            self.timer.stop()
            self.event_loop.quit()
            return

        elif self.hand_values["dealer"] > 21:
            self.update_status('dealer', 'bust')
            for player, status in self.player_status.items():
                if player != 'dealer' and status != "bust": 
                    self.update_status(player, 'win')
            self.timer.stop()
            self.event_loop.quit()
            return

    # Multiple Player Game Functions ------------------------
    def seat1_turn(self, agent):
        pass
   
    def seat2_turn(self):
        try:
            if self.hand_values['seat2'] > 21 or self.player_status['seat2'] in ['stand', 'double', 'blackjack']:
                try:
                    self.timer.stop()
                    self.event_loop.quit()
                    del self.timer
                except Exception:
                    pass
                return 

            set_agent_name(self, activate=True)

            # seat2 bets
            if not self.bets['seat2']:
                if self.game_mode == "TrainAgent":
                    self.action_bet = self.agent.choose_action_bet(self)
                else:
                    self.action_bet = self.agent.bet(self)
                
                self.bets["seat2"] = self.action_bet
                self.bankroll["seat2"] -= self.action_bet
                self.ui.label_seat2_budget_amount.setText("$"+str(self.bankroll["seat2"]))
                set_chips(self)
                return
            
            # Initial seat2's hand.
            display_cards(self, player='seat2')
            set_total(self, player="seat2")

            if not self.seat2_display_initial_hand: 
                self.seat2_display_initial_hand = True
                return

            # seat2 plays
            if self.game_mode == "TrainAgent":
                self.state_move = self.hand_values['seat2']
                self.action_move = self.agent.choose_action_move(self)
            else: 
                self.action_move = self.agent.move(self)

            self.func_hit('seat2') if self.action_move == "hit" else (self.func_stand('seat2') if self.action_move == "stand" else self.func_double('seat2'))

            if self.game_mode == "TrainAgent":
                state, action, exploration, next_state, reward, q = self.agent.update(self)
                update_console_list(self, state, action, exploration, next_state, reward, q)


        except Exception as err:
            print("An Exception occurred in seat2_turn:", err)
            traceback.print_exc()
            return


    # PIPELINES ---------------------------------------
    def pipeline_end_round(self):
        self.bankrupt_player = check_game_over(self)
        self.dealer_close_card_shown = True
        for player in self.players:
            display_cards(self, player=player)
            set_status_board(self, player=player)
            set_status_icon(self, player=player)
        set_total(self)
        move_buttons_usability(self, False)
        
        if self.game_mode != "OnePlayerGame":
            set_agent_name(self, activate=False)

        if self.bankrupt_player and self.game_mode != "TrainAgent":
            announce(self, subject='game over')
            set_cocktail_and_smoke(self, reset=True)

        elif not self.bankrupt_player and self.game_mode != "TrainAgent":
            announce(self, subject='round ends')
            set_cocktail_and_smoke(self)
            next_round_button_usability(self, True)
        
        payout(self)
        try:
            if self.timer.isActive():
                self.timer.stop()
                self.event_loop.quit()
                del self.timer
        except Exception:
           pass

        QApplication.processEvents()

    def pipeline_init_next_round(self):

        self.dealer_close_card_shown = False
        self.dealer_hand_is_initialized = False
        self.seat2_display_initial_hand = False
        self.seat1_display_initial_hand = False

        self.players = ()
        if self.game_mode == "OnePlayerGame":
            self.players = ('dealer', 'seat1')
        elif self.game_mode == "TrainAgent":
            self.players = ('dealer', 'seat2')
        elif self.game_mode == "SingleAgentGame":
            self.players = ('dealer', 'seat1', 'seat2')

        self.hands = {player: [] for player in self.players}
        self.hand_values = {player: 0 for player in self.players}
        self.player_status = {player: None for player in self.players}
        self.bets = {player: 0 for player in self.players if player != 'dealer'}
       
        for i in range(1, 10):
            label = self.findChild(QLabel, f"label_blackjack_text_{i}")
            label.setStyleSheet("")
        if self.round == 0:
            self.bankroll = {player: 10 for player in self.players if player != 'dealer'}
        
        self.round += 1
        
        set_budget(self)
        move_buttons_usability(self, False)
        bet_frame_usabilty(self, False)
        next_round_button_usability(self, False)
        set_chips(self, reset=True)
        display_cards(self, reset=True)
        set_status_icon(self, reset=True)
        set_status_board(self, reset=True)
        self.ui.label_round_number.setText(str(self.round))

        # 1) Players Bet
        if self.game_mode == "TrainAgent":
                self.countdown = 0.1 if self.ui.radioButton_training_speed_01.isChecked() else (0.5 if self.ui.radioButton_training_speed_05.isChecked() else 1)
        else:
            if not hasattr(self, "countdown"):
                self.countdown = 5
            else:
                self.countdown = 3

        self.init_timer(mode='init')  
        if self.ui.stackedwidget_content.currentIndex() == 0:
            return    
        
        if self.game_mode not in ["TrainAgent", "MultiAgentGame"]:
            set_bet_box(self, deactive=True)
            bet_frame_usabilty(self, False)
            self.bankroll["seat1"] = self.bankroll["seat1"] - self.bets["seat1"]

        # 2) Initialize Hands
        self.initialize_hands(self.players)

        for player in self.players:
            self.update_status(player=player, status="in play")
            set_total(self, player=player)
            display_cards(self, player=player)

        # 3) Check Blackjack
        if self.game_mode == "TrainAgent":
            # Skip the blackjack states for agent training.
            while True:
                is_round_going_on, blackjack_hands = self.pipeline_check_blackjack()
                if blackjack_hands:
                    print('Hand is initialized!')
                    self.initialize_hands(self.players)
                else: 
                    break

        else:
            is_round_going_on, blackjack_hands = self.pipeline_check_blackjack()

            if not is_round_going_on:
                self.pipeline_end_round()
                return
            else:
                if blackjack_hands == {"seat1"}:
                    self.countdown = 1
                    self.init_timer(mode="seat2 turn")
                    try:
                        self.timer.stop()
                        self.event_loop.quit()
                        del self.timer
                    except Exception:
                        pass
                    if self.ui.stackedwidget_content.currentIndex() == 0:
                        return
                else:
                    move_buttons_usability(self, True)
        
        QApplication.processEvents()


    def pipeline_check_blackjack(self):
        is_round_going_on = False
        blackjack_hands = check_blackjack(self)

        if blackjack_hands and self.game_mode == "TrainAgent":
            print(self.hands['seat2'])
            return is_round_going_on, blackjack_hands

        # Dealer & Seat 1 or Dealer & Seat 2
        elif blackjack_hands == {"dealer", "seat1"} or blackjack_hands == {"dealer", "seat2"}:
            for player in blackjack_hands:
                self.update_status(player=player, status="push")
            for player, status in self.player_status.items():
                if status == "in play":
                    self.update_status(player=player, status="lose")
        
        elif blackjack_hands == {"dealer", "seat1", "seat2"}:
            for player in blackjack_hands:
                self.update_status(player=player, status="push")

        elif blackjack_hands == {"dealer"}:
            self.update_status(player="dealer", status="blackjack")
            for player, status in self.player_status.items():
                if status == "in play":
                    self.update_status(player=player, status="lose")
        
        elif blackjack_hands and self.game_mode == "OnePlayerGame":
            self.update(player="seat1", status="blackjack")
            self.update(player="delaer", status="lose")
        
        elif blackjack_hands:
            for player in blackjack_hands:
                self.update_status(player=player, status="blackjack")
            if len(blackjack_hands) == 2:
                self.update_status(player="dealer", status="lose")
            else:
                is_round_going_on = True
        else:
            is_round_going_on = True

        for player in self.players:
            set_status_board(self, player=player)
            set_status_icon(self, player=player)
        return is_round_going_on, blackjack_hands
            

    def pipeline_reset_game_page(self):
        for i in range(1, 10):
            label = self.findChild(QLabel, f"label_blackjack_text_{i}")
            label.setStyleSheet("")
        try:
            move_buttons_usability(self, False)
            bet_frame_usabilty(self, False)
            display_cards(self, True)
            set_status_icon(self, reset=True)
            set_chips(self, True)
            set_cocktail_and_smoke(self, True)
            if not hasattr(self, "train_timer"):
                announce(self, True)
            set_status_board(self, reset=True)
            set_bet_box(self, True)
            set_budget(self, True)
            set_agent_name(self, reset=True)
            set_seat(self, reset=True)
        except Exception:
            pass
        
        self.ui.lineEdit_agentfilename.setText("")
        self.ui.spinBox_training_episode.setValue(2500)
        self.ui.radioButton_training_episode.setChecked(False)
        self.ui.spinBox_rounds_without_losing.setValue(20)
        self.ui.radioButton_rounds_without_losing.setChecked(False)
        self.ui.spinBox_achieved_budget.setValue(1000)
        self.ui.radioButton_achieved_budget.setChecked(False)
        self.ui.radioButton_training_speed_1.setChecked(True)
        self.ui.label_stats_exploration_rate.setText("Exploration Rate:")
        self.ui.label_stats_game_count.setText("Game Count:")
        self.ui.label_stats_episode.setText("Total Episode (Round):")
        self.ui.label_stats_mab.setText("Max Achieved Budget:")
        update_last_rounds_list(self, reset=True)
        update_console_list(self, reset=True)
        QApplication.processEvents()
