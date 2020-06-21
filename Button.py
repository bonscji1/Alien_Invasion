import pygame.font

class Button:

    def __init__(self,game,msg):
        '''init button atributes'''
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        #dimensions of the button
        self.width, self.height = 200,50
        self.button_color = (0,0,250)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        #build the rect and center it
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #prep button message
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        '''turn msg into image and center it in the button'''
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''Draw button on the screen'''
        #draw blank button then draw message
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)