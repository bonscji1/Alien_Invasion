
import pygame.font

class Scoreboard:
    '''Class to track scoring information'''

    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        #Font settings
        self.text_color = (30,150,30)
        self.high_score_color = (150,30,30)
        self.level_color = (150,150,30)
        self.font = pygame.font.SysFont(None,48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        '''turn score into rendered image, then display it at top right'''
        rounded_score = round(self.stats.score, -1)
        #score_str = "{:,}".format(rounded_score)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        #Display score at top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right-20
        self.score_rect.top = 20

    def prep_high_score(self):
        '''turn high score into rendered image'''
        rounded_high_score = round(self.stats.high_score, -1)
        high_score_str = f"{rounded_high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.high_score_color, self.settings.bg_color)

        # Display high score at top middle
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        level_str = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.level_color, self.settings.bg_color)

        # Display high score at top middle
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.left = 20
        self.level_image_rect.top = self.score_rect.top

    def show_score(self):
        '''Draw score and level to screen'''
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image, self.level_image_rect)

    def check_high_score(self):
        '''check if there is new high score'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
