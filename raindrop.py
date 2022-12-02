import pygame

class Raindrop:
    def __init__(self):
        self.image = pygame.image.load('images/raindrop.bmp')
        self.offset = 0

    def draw(self, screen):
        screen.blit(self.image, (254, 0 + self.offset))

    def fall(self, max_offset):
        self.offset += 1
        if self.offset > max_offset:
            self.offset = 0