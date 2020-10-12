import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #represents a single alien in the fleet

    def __init__(self, ai_game):
        #initialize alien & starting position
        super().__init__()
        self.screen = ai_game.screen

        #load alien image and set its rect attribute
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        #start each new alien near top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store alien's exact horizontal position
        self.x = float(self.rect.x)