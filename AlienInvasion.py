# from python crash course

import sys
import pygame

from Settings import Settings
from Ship import Ship
from Bullet import Bullet
from Alien import Alien


class AlienInvasion:
    '''Main class, base of the program'''

    def __init__(self):
        '''initialize game and resources'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        # ship
        self.ship = Ship(self)

        # bullets
        self.bullets = pygame.sprite.Group()

        # alien
        self.aliens = pygame.sprite.Group()

        self._create_invasion()

    # helper method - start with _(underscore)

    def _update_screen(self):
        # basic redraw
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

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

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _create_invasion(self):
        '''create fleet of invading aliens'''
        # settings for fleet
        test_alien = Alien(self)
        alien_width, alien_height = test_alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        num_of_aliens_x = available_space_x // (2 * alien_width) + 1  # +1 is my correction
        available_space_y = self.settings.screen_height - (3 * alien_height)
        num_of_aliens_y = available_space_y // (2 * alien_height) - self.settings.alien_buffer_zone

        for row_number in range(num_of_aliens_y):
            for alien_number in range(num_of_aliens_x):
                self._create_alien(alien_number, row_number)

    def _update_aliens(self):
        '''
        Check if fleet hits an edge, then update alien position
        '''
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        '''Respond if any alien hit an edge'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''Drop fleet and change direction'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_speed_vertical

        self.settings.alien_moving_right = not self.settings.alien_moving_right
        print(self.settings.alien_moving_right)

    def run(self):
        '''Main loop'''
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._remove_obsole_bullets()
            self._update_aliens()
            self._update_screen()


if __name__ == "__main__":
    main = AlienInvasion()
    main.run()
