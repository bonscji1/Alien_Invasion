import pygame

class Ship:
    '''Ship class'''

    def __init__(self,game):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        #load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start at mid bottom
        self.rect.midbottom = self.screen_rect.midbottom

        #movement
        self.moving = False
        self.moving_x = 0
        self.x = float(self.rect.x)





    def update(self):
        '''update ship position'''
        if self.moving:
            self.x += self.moving_x
            # do not move out of range
            if self.rect.right > self.screen_rect.right:
                pass
                self.x = self.screen_rect.right-self.rect.w
            if self.rect.left < 0:
                self.x = 0

            self.rect.x = self.x

    def blitme(self):
        '''draw sbip at current location'''
        self.screen.blit(self.image, self.rect)
