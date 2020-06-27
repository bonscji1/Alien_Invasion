# from python crash course

import sys
import pygame

from time import sleep

from Settings import Settings
from Ship import Ship
from Bullet import Bullet
from Alien import Alien
from Game_stats import Game_stats
from Button import Button
from Scoreboard import Scoreboard



class AlienInvasion:
    '''Main class, base of the program'''

    def __init__(self):
        '''initialize game and resources'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.stats = Game_stats(self)
        self.score = Scoreboard(self)

        pygame.display.set_caption("Alien Invasion")

        # ship
        self.ship = Ship(self)

        # bullets
        self.bullets = pygame.sprite.Group()

        # alien
        self.aliens = pygame.sprite.Group()

        self._create_invasion()

        #control
        self.play_button = Button(self,"Play")


    # helper method - start with _(underscore)

    def _update_screen(self):
        # basic redraw
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        #draw score
        self.score.show_score()

        #Draw button if game is inactive
        if not self.settings.game_active:
            self.play_button.draw_button()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_play_button(mouse_position)

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

    def _check_play_button(self, mouse_position):
        '''start new game when player clicks play'''
        if self.play_button.rect.collidepoint(mouse_position) and not self.settings.game_active:
            self._game_reset()

            self.settings.game_active = True
            #hide mouse cursor
            pygame.mouse.set_visible(False)



    def _game_reset(self):
        '''Reset game'''

        self.stats.reset_stats()
        self.settings.init_dynamic_settings()
        self.score.prep_score()
        # get rid of previous game objects
        self.aliens.empty()
        self.bullets.empty()
        self._create_invasion()
        self.ship.center_ship()


    def _fire_bullet(self):
        '''create bullet and add it to bullets'''
        self.bullets.add(Bullet(self))

    def _remove_obsole_bullets(self):
        '''remove obsolete bullets and aliens if hit'''
        for bullet in self.bullets:
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _alien_bullet_collision(self):
        #Check for bullet sthat have hit aliens
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, self.settings.bullet_single_kill, True)

        if collisions:
            for alien in collisions.values():
                self.stats.score += self.settings.alien_points*len(alien)
                self.score.prep_score()
                self.score.check_high_score()


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
        num_of_aliens_x = available_space_x // (2 * alien_width) + 1  # +1 is my correction - remove if game too hard
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
        self._alien_ship_collision()
        self._check_aliens_landed()

    def _alien_ship_collision(self):
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _ship_hit(self):
        '''Ship has been hit logic'''
        #remove ship life if you can
        if self.stats.ship_left>0:
            self.stats.ship_left -= 1
            # reset game state
            self.aliens.empty()
            self._reset_state()
            self.ship.center_ship()
            #pause game for a bit
            sleep(self.settings.hit_freeze_time)
        else:
            self._game_over()



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


    def _code_relentless_horde(self):
        if not self.aliens:
            self._reset_state()
            self.settings.increase_speed()

    def _check_aliens_landed(self):
        '''check if aliens reached bottom of screen'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _reset_state(self):
        '''Destroy bullets, reset aliens'''
        self.bullets.empty()
        self._create_invasion()

    def _update_game_state(self):
        self._remove_obsole_bullets()
        self._alien_bullet_collision()
        self._code_relentless_horde()

    def _game_over(self):
        self.settings.game_active = False
        self.stats.save_high_score(self.stats.high_score)
        pygame.mouse.set_visible(True)

    def run(self):
        '''Main loop'''
        while True:
            self._check_events()

            if self.settings.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_game_state()
                self._update_aliens()
            self._update_screen()


if __name__ == "__main__":
    main = AlienInvasion()
    main.run()
