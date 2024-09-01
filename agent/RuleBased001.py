import random

class Rubi001:
    """
    Bet Strategy:
        - Bankroll > 20: Bet $5.
        - Bankroll between 10 and 20: Bet $3.
        - Bankroll between 5 and 10: Bet $2.
        - Bankroll < 5: Bet $1.
    
    Game Strategy:
        Hand ≤ 11: 100% chance to hit.
        Hand = 12: 20% chance to double, 80% chance to hit.
        Hand = 13: If bankroll allows, 60% chance to double, 30% chance to hit, 10% chance to stand.
        Hand = 14, 15, 16: 5% chance to double, 20% chance to stand, 75% chance to hit.
        Hand = 17-18: 15% chance to hit, 85% chance to stand.
        Hand = 19: 5% chance to hit, 95% chance to stand.
        Hand = 20-21: 100% chance to stand.

    About Rubi001:
    Rubi001's biggest weakness is their inability to develop a strategy based on the dealer's starting face-up card. 
    Their game and betting strategy is not bad at all."
    """
    def __init__(self):
        print('Rubi001 in the house')

    def bet(self, bankroll:int) -> int:

        if bankroll > 20:
            return 5
        elif bankroll > 10:
            return 3
        elif bankroll > 5:
            return 2
        else:
            return 1

    def action(self, hand:int) -> str: 

        if hand <= 11: 
            hit, stand, double = 100, 0, 0
        elif hand == 12:
            hit, stand, double = 80, 0, 20
        elif hand == 13:
            hit, stand, double = 30, 10, 60
        elif hand <= 16: 
            hit, stand, double = 75, 20, 5
        elif hand <= 18: 
            hit, stand, double = 15, 85, 0
        elif hand == 19:
            hit, stand, double = 5, 95, 0
        elif hand <= 21:
            hit, stand, double = 0, 100, 0

        actions = ['hit', 'stand', 'double']
        weights = [hit, stand, double]

        action = random.choices(actions, weights)[0]

        return action
    

        

