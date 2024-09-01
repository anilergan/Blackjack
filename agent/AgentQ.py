
"""
----------------------- Agent Bet:

reward = (total_profit + latest_profit*2) / 3

state = bankroll

action = bet (categoric) [0,0,0,0,0,0,0,0,0,1]

---------------------------------
------------- Agent Taking Action:

reward = lp

state = [
- bet (numeric), min:1, max:10
- dealer hand (numeric), min:1, max: 11
- agent hand value (numeric), min: 1, max: 21
- is there any Ace value in agent hand with 11 value? (binary),
]

action = [hit, stand, double]

---------------------------------


"""


class AgentQ:
    """
    """
    def __init__(self):
        print('AgentQ in the house')

    def bet(self) -> int:
        pass

    def action(self) -> str:
        pass