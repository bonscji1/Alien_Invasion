#from python crash course

import sys
import pygame

from Settings import Settings
from Ship import Ship
from Bullet import Bullet


class AlienInvasion:
    '''Main class, base of the program'''

    def __init__(self):
        '''initialize game and resources'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigh))

        pygame.display.set_caption("Alien Invasion")

        #ship
        self.ship = Ship(self)

        #bullets
        self.bullets = pygame.sprite.Group()

    #helper method - start with _(underscore)


    def _update_screen(self):
        # basic redraw
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

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

        elif event.key == pygame.K_SPACE:
            if len(self.bullets) < self.settings.bullets_allowed:
                self._fire_bullet()

        if event.key == pygame.K_d:
            # move ship to the right
            self.ship.moving = True
            self.ship.moving_x = self.settings.ship_speed
        if event.key == pygame.K_a:
            # move ship to the left
            self.ship.moving = True
            self.ship.moving_x = -self.settings.ship_speed

    def _fire_bullet(self):
        '''create bullet and add it to bullets'''
        self.bullets.add(Bullet(self))

    def _remove_obsole_bullets(self):
        for bullet in self.bullets:
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)



    def run(self):
        '''Main loop'''
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            self._remove_obsole_bullets()

            self._update_screen()

if __name__ == "__main__":
    main = AlienInvasion()
    main.run()