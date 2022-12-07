import pygame

class Duty_Van1:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('images/duty_van.png')
        self.rect = self.image.get_rect()
        self.x = 128*2

        # Store a decimal value for the ship's horiz pos
        self.x = float(self.rect.x)

        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def blit(self, screen):
        screen.blit(self.image, (self.x, self.rect.midbottom))

    def update(self):
