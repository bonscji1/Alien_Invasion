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
            self.ship_speed = 1.5
            self.ship_limit = 3

            #Bullet setting
            self.bullet_speed = 1.5
            self.bullet_width = 300#3
            self.bullet_height = 15
            self.bullet_color = (200,60,60)
            self.bullets_allowed = 3
            self.bullet_single_kill = False

            #aliens settings
            self.alien_buffer_zone = 4
            self.alien_speed_horizontal = 0.5
            self.alien_speed_vertical = 100#10
            self.alien_moving_right = True

            #End settings
            self.hit_freeze_time = 1
            self.game_active = True
