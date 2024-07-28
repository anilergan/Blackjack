
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

        self.player_loss_profit = {

        }

        self.players_stand = set()
        self.players_bust = set()

        self.stakes = {
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
    


    def update_status(self, player:str, status:str):
        possible_status = ['in play', 'stand', 'win', 'draw', 'bust', 'double', 'double bust', 'double win']
        if status not in possible_status:
            raise Exception('Status could not be updated: VALID STATUS.')
        
        if player not in self.players:
            raise Exception('Status could not be updated: VALID PLAYER')
        
        self.player_status[player] = status
            

        

