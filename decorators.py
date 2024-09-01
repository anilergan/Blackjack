
def stand_decorator(func):
    def wrapper(self, *args, **kwargs):

        check = func(self, *args, **kwargs)
        if check == 'interrupt': return

        self.move_buttons_usability(False)
        self.set_move_box(deactive=True)
        
        self.set_total_and_status()
        self.set_status_board()
        
        # if there is no player whose status 'in play' (exclude dealer)
        if list(self.player_status.values()).count('in play') == 1:
            self.countdown = 0
            self.init_timer(mode='dealer_hit')
            
        # so opponent is still in play
        elif list(self.player_status.values()).count('in play') > 1:
            while True:
                self.init_timer(mode='agent_hit')
                if not self.timer.isActive():
                    break

                

    return wrapper

