#from python crash course

import sys
import pygame

from Settings import Settings
from Ship import Ship


class AlienInvasion:
    '''Main class, base of the program'''

    def __init__(self):
        '''initialize game and resources'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigh))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        #ship speed
        self.ship_speed = 1.5

    #helper method - start with _(underscore)


    def _update_screen(self):
        # basic redraw
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # make most recent screen visible
        pygame.display.flip()

    def _check_events(self):
        '''keyboard and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keyDown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyUP(event)


    def _check_keyUP(self, event):
        if event.key == pygame.K_a or event.key == pygame.K_d:
            self.ship.moving = False
            self.ship.moving_x = 0


    def _check_keyDown(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit(0)

        if event.key == pygame.K_d:
            # move ship to the right
            self.ship.moving = True
            self.ship.moving_x = self.ship_speed
        if event.key == pygame.K_a:
            # move ship to the left
            self.ship.moving = True
            self.ship.moving_x = -self.ship_speed


    def run(self):
        '''Main loop'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

if __name__ == "__main__":
    main = AlienInvasion()
    main.run()