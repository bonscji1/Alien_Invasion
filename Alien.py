
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''class to represent single alien'''

    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        #load alien image
        self.image = pygame.image.load('images/Invader1.bmp')
        self.rect = self.image.get_rect()

        #start alien at top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


    def check_edges(self):
        '''return true if alien hit edge'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True


    def update(self):
        '''Move aliens'''
        if self.settings.alien_moving_right:
            self.x += self.settings.alien_speed_horizontal
        else:
            self.x -= self.settings.alien_speed_horizontal
        self.rect.x =self.x

