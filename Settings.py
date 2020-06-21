class Settings:
        '''Settings for the game'''

        def __init__(self):
            '''initial settings'''
            #Screen
            self.screen_width = 1200
            self.screen_height = 800
            self.bg_color = (0,0,0)
            self.fullScreen = False

            # ship settings

            self.ship_limit = 3

            #Bullet setting
            self.bullet_width = 5
            self.bullet_height = 15
            self.bullet_color = (200,60,60)
            self.bullets_allowed = 3
            self.bullet_single_kill = False

            #aliens settings
            self.alien_buffer_zone = 5
            self.alien_speed_vertical = 10


            #End settings
            self.hit_freeze_time = 1
            self.game_active = False

            #quick changeup to game
            self.speedup_scale = 1.5

            self.init_dynamic_settings()

        def init_dynamic_settings(self):
            '''init dynamic settings'''

            #ship
            self.ship_speed = 1.5

            #bullet
            self.bullet_speed = 2

            #alien
            self.alien_speed_horizontal = 0.5
            self.alien_moving_right = True

        def increase_speed(self):
            '''increase speed of the game'''
            self.ship_speed *= self.speedup_scale
            self.bullet_speed *= self.speedup_scale
            self.alien_speed_horizontal *= self.speedup_scale