import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''class to manage bullets'''

    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        #creat bullet rec at (0,0), then set it to correct position
        self.rect =pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        #store as decimal value
        self.y = float(self.rect.y)


    def update(self):
        '''move the bullet up'''
        self.y -= self.settings.bullet_speed
        #update rect position
        self.rect.y =self.y


    def draw_bullet(self):
        '''draw bullet on the screen'''
        pygame.draw.rect(self.screen,self.color, self.rect)