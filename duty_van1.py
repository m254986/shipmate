import pygame

class Duty_Van1:
    def __init__(self):
        self.image = pygame.image.load('images/duty_van.png')
        self.rect = self.image.get_rect()
        self.x = 128*2

    def blit(self, screen):
        screen.blit(self.image, (self.x, self.rect.midbottom))

    def update(self):
