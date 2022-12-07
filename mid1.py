import pygame
from random import randint
import time

class Mid1:
    def __init__(self):
        self.image = pygame.image.load('images/mid.png')
        self.mid_rect = self.image.get_rect()
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
        if time == 5:
            self.offset += 10

            # how to make appear smoothly from top?