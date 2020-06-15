class Settings:
        '''Settings for the game'''

        def __init__(self):
            '''initial settings'''
            #Screen
            self.screen_width = 1200
            self.screen_heigh = 800
            self.bg_color = (0,0,0)
            self.fullScreen = False

            # ship speed
            self.ship_speed = 1.5

            #Bullet setting
            self.bullet_speed = 1.0
            self.bullet_width = 3
            self.bullet_height = 15
            self.bullet_color = (200,60,60)
            self.bullets_allowed = 3
