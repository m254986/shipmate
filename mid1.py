import pygame
from random import randint

# how to make fall cleanly form top?
# add a beer?
class Mid1:
    def __init__(self):
        self.image = pygame.image.load('images/mid.png')
        self.offset = 0
        self.x = 128*2
        self.y = 128*2

    def blit(self, screen):
        screen.blit(self.image, (self.x, 0 + self.offset))

    def update(self, max_offset):
        self.offset += 3
        if self.offset > max_offset:
            self.offset = 0
            self.x = randint(128, 128*4)

            # how to make appear smoothly from top?