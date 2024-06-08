
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
            'table1': [],
            'table2': [],
            'table3': [],
        }

        self.players = set(['dealer', 'agent', 'opp1', 'opp2'])