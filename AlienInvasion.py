#from python crash course

import sys
import pygame


class AlienInvasion:
    '''Main class, base of the program'''

    def __init__(self):
        '''initialize game and resources'''
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        #set background color
        self.bgc = (255,255,255)



    def run(self):
        '''Main loop'''
        while True:
            #keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # basic redraw
            self.screen.fill(self.bgc)

        #make most recent screen visible
        pygame.display.flip()

if __name__ == "__main__":
    main = AlienInvasion()
    main.run()