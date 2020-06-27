

class Game_stats:
    '''Statistics for the game'''

    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()
        self.high_score = 0

    def reset_stats(self):
        '''init changeable statistics'''
        self.ship_left = self.settings.ship_limit
        self.score = 0