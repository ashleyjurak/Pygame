import pygame.font #renders text to screen

class Button:

    def __init__(self, ai_game, msg): #msg contains button's text
        #initialize button attributes
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #set dimensions and properties of the button
        self.width, self.height = 200,50
        self.button_color = (0, 255, 0) #bright green (r,g,b)
        self.text_color = (255, 255, 255) #white text
        self.font = pygame.font.SysFont(None, 48) #(default font, size)

        #build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #prep button message (only once)
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        #turn msg into redered image and center text on button
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) #turns text into image, True = edges of text smoother, text background = button color
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #draw blank button then message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)