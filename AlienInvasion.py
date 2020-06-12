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
        self.setings = Settings()
        self.screen = pygame.display.set_mode((self.setings.screen_width, self.setings.screen_heigh))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)




    def run(self):
        '''Main loop'''
        while True:
            #keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # basic redraw
            self.screen.fill(self.setings.bg_color)
            self.ship.blitme()


            #make most recent screen visible
            pygame.display.flip()

if __name__ == "__main__":
    main = AlienInvasion()
    main.run()