import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #represents a single alien in the fleet

    def __init__(self, ai_game):
        #initialize alien & starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load alien image and set its rect attribute
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        #start each new alien near top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store alien's exact horizontal position
        self.x = float(self.rect.x)
    
    def check_edges(self):
        #return true if alien is at edge
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        #move aliens to right or left
        self.x += (self.settings.alien_speed * self.settings.fleet_direction) #tracks alien's exact position using decimal values
        self.rect.x = self.x

