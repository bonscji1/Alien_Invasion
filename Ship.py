import pygame

class Ship:
    '''Ship class'''

    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        #load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start at mid bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''draw sbip at current location'''
        self.screen.blit(self.image, self.rect)

