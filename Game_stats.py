
import json

FILE = "high_score.json"

class Game_stats:
    '''Statistics for the game'''



    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()

        #high score stats
        self.high_score = self.load_high_score()



    def reset_stats(self):
        '''init changeable statistics'''
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        try:
            with open(FILE) as f:
                number = json.load(f)
        except FileNotFoundError:
            return 0
        else:
            return number

    def save_high_score(self,number):
        with open(FILE, 'w') as f:
            json.dump(number, f)