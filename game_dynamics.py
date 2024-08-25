
class BlackjackDynamics():
    def __init__(self):
        # GAME DYNAMICS -----------------------------
         # Shoe: Blackjack masasında kullanılan ve birden fazla deste kartın saklandığı cihaza "shoe" denir. Krupiyer, kartları bu ayakkabıdan çeker ve dağıtır.
        
        number_cards = ('2','3','4','5','6','7','8','9','10')
        face_cards = ('K', 'Q', 'J', 'A')
        self.deck = number_cards + face_cards

        self.card_values = {
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


        # Hands:  Bir oyuncunun elindeki kartlara "hand" denir. Blackjack'te oyuncular ellerini oluştururken veya kararlar alırken "hand" terimi sıkça kullanılır.
        self.hands = {
            'dealer': [],
            'seat1': [],
            'seat2': [],
        }

        self.hand_values = {
            'dealer': 0,
            'seat1': 0,
            'seat2': 0,
        } 

        self.player_status = {
            'dealer': None,
            'seat1': None,
            'seat2': None
        }
       
        self.house = 100  # it's random number but 100 picked to make it easy to calculate gain/loss of house



    def update_hand_values(self):
        for player, hand in self.hands.items():
            ace_num = hand.count('A')
            total = 0
            for card in hand:
                total += self.card_values[card]
                if total > 21 and ace_num != 0:
                    total -= 10
                    ace_num -= 1
            self.hand_values[player] = total
    


    def update_status(self, player:str=None, status:str=None):


        possible_status = ['in play', 'blackjack', 'stand', 'win', 'push', 'bust', 'double', 'bankrupt']
        possible_players = ['dealer', 'seat1', 'seat2']
        if (status not in possible_status or player not in possible_players) and (status is not None and player is not None):
            print(f'Status could not be updated: Valid Status or Player!\nStatus: {status}\nPlayer: {player}')

        # Menuel
        elif status is not None and player is not None:
            self.player_status[player] = status
            return
        
        # Auto
        for p, v in self.hand_values.items():
            if v > 21:
                self.player_status[p] = 'bust'
        

        if self.player_status['dealer'] == 'bust':
            for p, s in self.player_status.items():
                if s is not None and s not in ['bust', 'bankrupt']: self.player_status[p] = 'win'
        
        
        if self.player_status['dealer'] == 'stand':
            for p, s in self.player_status.items():
                if p == 'dealer': continue
                if s in ['stand', 'double'] and self.hand_values[p] > self.hand_values['dealer']:
                    self.player_status[p] = 'win'
                
                elif s in ['stand', 'double'] and self.hand_values[p] == self.hand_values['dealer']:
                    self.player_status[p] = 'push'
                    self.player_status['dealer'] = 'push'
                
                elif s in ['stand', 'double'] and self.hand_values[p] < self.hand_values['dealer']:
                    self.player_status['dealer'] = 'win'
        
        if list(self.player_status.values()).count('blackjack') == len(self.players):
            for player in self.players:
                self.player_status[player] = 'push'
        
        




            

        

