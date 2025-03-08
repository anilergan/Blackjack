import random
import pickle
import os

TRAINED_AGENTS_PATH = "src\\agent\\trained_agents"

class QAgent():
    def __init__(self,
                 alpha=0.1,
                 gamma=0.99,     
                 epsilon=1.0,
                 epsilon_decay=0.999,
                 min_epsilon=0.01, 
                 initial_budget=10,
                 seat="seat2"):
        # Learning parameters
        self.alpha = alpha # learning rate
        self.gamma = gamma # discount factor
        self.epsilon = epsilon # exploration probability
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = min_epsilon
        
        # Separate Q-tables for the two decision phases:
        # Q-table for betting (state: dealer's open card)
        # Actions: possible bet amounts from 1 to 10
        self.q_table_bet = {} 
        
        # Q-table for move decisions (state: player’s hand value)
        # Actions: 'hit', 'stand', or 'double'
        self.q_table_move = {}
        
        # Statistics and tracking variables
        self.initial_budget = initial_budget
        self.max_budget = initial_budget
        self.total_games = 0  # number of rounds played (across games)
        self.episode = 0      # total episodes (training rounds)

        self.data = {
            "q_table_bet": self.q_table_bet,
            "q_table_move": self.q_table_move,
        }
        self.seat = seat

    
    def save_trained_agent(self, path):
        # The string keys in self.data must have the same name as the relevant variables to be saved!
        self.data = {
            "q_table_bet": self.q_table_bet,
            "q_table_move": self.q_table_move,
        }
        with open(path, "wb") as f:
            pickle.dump(self.data, f)
        print(f"Trained agent saved to {path}")

    def load_trained_agent(self, path):
        if os.path.exists(path):
            try:
                with open(path, "rb") as f:
                    data = pickle.load(f)
                    self.q_table_bet = data.get("q_table_bet", {})
                    self.q_table_move = data.get("q_table_move", {})
                print(f"Trained agent loaded from {path}")
            except Exception as e:
                print(f"Error loading trained agent from {path}: {e}")
        else:
            print(f"No trained agent found at {path}")

    # ----- Q-table Utility Functions -----
    def _ensure_bet_state(self, state):
        if state not in self.q_table_bet:
            # Initialize all possible bet actions (1 to 10) to 0.0
            self.q_table_bet[state] = {bet: 0.0 for bet in range(1, 11)}
    
    def _ensure_move_state(self, state):
        if state not in self.q_table_move:
            # Initialize actions for move decision with Q-value 0.0
            self.q_table_move[state] = {'hit': 0.0, 'stand': 0.0, 'double': 0.0}
    
    # ----- Action Selection (Epsilon-Greedy) -----
    def choose_action_bet(self, BJself):
        # STATE = (dealer_open_card)
        STATE = (BJself.bankroll[self.seat])
        # CONDITION
        bankroll = BJself.bankroll['seat2']

        self._ensure_bet_state(STATE)
        if random.random() < self.epsilon:
            # Explore: choose a random bet between 1 and the lesser of 10 or the bankroll
            up_range = min(10, bankroll)
            if up_range == 1:
                return up_range
            else:
                return random.randint(1, up_range)
        else:
            # Filter bets to only include those less than or equal to the bankroll.
            # Assuming keys are stored as integers or strings that represent integers:
            valid_bets = {
                int(bet): q_value 
                for bet, q_value in self.q_table_bet[STATE].items() 
                if int(bet) <= bankroll
            }
            if valid_bets:
                # Return the bet with the highest Q-value among the valid bets.
                return max(valid_bets, key=valid_bets.get)
            else:
                # Fallback: if no valid bets are available, return a default value (e.g., 1)
                return 1

    def choose_action_move(self, BJself):
        # STATE = (hand_value, as_count)
        STATE = (BJself.hand_values[self.seat], BJself.hands[self.seat].count('A'))

        # CONDITION 
        bet = BJself.bets[self.seat]
        bankroll = BJself.bankroll[self.seat]

        self._ensure_move_state(STATE)
        # Determine valid moves based on bankroll
        valid_moves = ['hit', 'stand', 'double'] if bet <= bankroll else ['hit', 'stand']

        print("bankroll:", bankroll, "bet:", bet, "valid:", valid_moves)

        
        if random.random() < self.epsilon:
            self.exploration = True
            # Explore: randomly choose among valid moves
            return random.choice(valid_moves)
        else:
            self.exploration = False
            # Exploit: choose the move with the highest Q-value among the valid moves
            # Filter the Q-table entries to only include valid moves
            q_values = {move: self.q_table_move[STATE][move] for move in valid_moves if move in self.q_table_move[STATE]}
            return max(q_values, key=q_values.get)

    # ----- Q-Value Update Functions -----
    def update(self, BJself):
        
        # ---------- MOVE ----------
        ACTION = BJself.action_move
        REWARD = self.__reward_move(
            BJself.player_status[self.seat], 
            ACTION
        )
        STATE = (
            BJself.hand_value_before,
            BJself.hands[self.seat].count('A')
        )

        NEXT_STATE = (
            BJself.hand_values[self.seat], 
            BJself.hands[self.seat].count('A')
        )       
    
        self._ensure_move_state(STATE)
        self._ensure_move_state(NEXT_STATE)

        max_next_q = max(self.q_table_move[NEXT_STATE].values())
        # Q-learning update rule:
        self.q_table_move[STATE][ACTION] += self.alpha * (REWARD + self.gamma * max_next_q - self.q_table_move[STATE][ACTION])

        move_summary = (STATE, ACTION, self.exploration, NEXT_STATE, REWARD, self.q_table_move[STATE][ACTION])
        # ---------- BET ----------
        # The only way we can evaluate the betting action is to see if the dealer takes action and if there is a bust.
        if BJself.dealer_close_card_shown:
            ACTION = BJself.action_bet
            REWARD = self.__reward_bet(BJself.player_status[self.seat], ACTION, BJself.bets[self.seat])
            STATE = (BJself.bankroll[self.seat])
            NEXT_STATE = (BJself.hand_values['dealer'])
            self._ensure_bet_state(STATE)
            self._ensure_bet_state(NEXT_STATE)

            max_next_q = max(self.q_table_bet[NEXT_STATE].values())
            # Q-learning update rule:
            self.q_table_bet[STATE][ACTION] += self.alpha * (REWARD + self.gamma * max_next_q - self.q_table_bet[STATE][ACTION])
        
        self.epsilon = max(self.min_epsilon, self.epsilon * self.epsilon_decay)

        return move_summary

        
    
    def __reward_move(self, status, action):
        if status not in ["bust", "lose", "bankrupt"]:
            return 1 if action != "double" else 2
        elif status in ["bust", "lose", "bankrupt"]:
            return -1 if action != "double" else -2

    
    def __reward_bet(self, status, action, bet):
        reward_move = self.__reward_move(status, action)
        reward_bet = reward_move * bet if status != "bankrupt" else reward_move * bet * 2
        if status == "bankrupt": 
            print("actually reward:", reward_move * bet, "but bankrupt! So:", reward_bet)
        return reward_bet

        
    
    # ----- Decision Functions for Use in the Game -----
    def bet(self, BJself):
        """
        Return a bet amount based on the current Q-values.
        The bet state is based on the dealer's open card.
        """
        STATE = (BJself.bankroll[self.seat])

        self._ensure_bet_state(STATE)
        # Bankroll'ı aşmayan geçerli bahisleri filtrele
        valid_bets = {
            int(BJself.bets[self.seat]): q_value 
            for BJself.bets[self.seat], q_value in self.q_table_bet[STATE].items() 
            if int(BJself.bets[self.seat]) <= BJself.bankroll[self.seat]
        }
        # Eğer geçerli bahis varsa, en yüksek Q-değerine sahip olanı seç
        if valid_bets:
            best_action = max(valid_bets, key=valid_bets.get)
        else:
            # Geçerli bahis yoksa varsayılan olarak 1 döndür
            best_action = 1
        return best_action

    def move(self, BJself):
        
        """
        Return the move decision ('hit', 'stand', or 'double') based on the current Q-values.
        The move state is defined by the player's hand value.
        """
        STATE = (BJself.hand_values[self.seat], BJself.hands[self.seat].count('A'))

        bet = BJself.bets[self.seat]
        bankroll = BJself.bankroll[self.seat]

        self._ensure_move_state(STATE)
        
        # Bankroll'a göre geçerli hamleleri belirle
        valid_moves = ['hit', 'stand', 'double'] if bet <= bankroll else ['hit', 'stand']

        print('self.q_table_move[STATE]["hit"]:', self.q_table_move[STATE]["hit"])
        # Q-tablosundaki değerleri sadece geçerli hamleler için filtrele
        q_values = {move: self.q_table_move[STATE][move] for move in valid_moves if move in self.q_table_move[STATE]}
        best_action = max(q_values, key=q_values.get)
        return best_action
