
class SimpleDecisionMakingAgent():
    def __init__(self, seat='seat2'):
        print('Simple Decision Making Agent in the house!')
        self.seat = seat


    def move(self, BJself):
        hand_value = BJself.hand_values[self.seat]
        bet = BJself.bets[self.seat]
        bankroll = BJself.bankroll[self.seat]
        if hand_value in [12, 13] and bankroll >= bet:
            return "double" #double
        elif hand_value < 16:
            return "hit" #hit
        else:
            return "stand" #stand
    
    def bet(self, BJself):
        bankroll = BJself.bankroll[self.seat]
        bet = 2 if bankroll >= 2 else bankroll
        return bet
        