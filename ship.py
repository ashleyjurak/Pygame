import pygame
from pygame.sprite import Sprite

#never make more than one ship, just recenter same ship instance when it has been hit

class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__() #allows us to create group of ships
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('ship.bmp')
        self.rect = self.imagve.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        #center ship on screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
