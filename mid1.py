import pygame
from random import randint
import time

class Mid1:
    def __init__(self, screen):
        self.image = pygame.image.load('images/mid.png')
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.mid_rect = self.image.get_rect()
        self.mid_rect.midbottom = self.screen_rect.midbottom

        self.offset = 0
        self.x = 128*2
        self.y = 128*2
        self.time = pygame.time.get_ticks()

    def blit(self, screen):
        screen.blit(self.image, (self.x, 0 + self.offset))

    def update(self, max_offset, time):
        self.offset += 10
        if self.offset > max_offset:
            self.offset = 0
            self.x = randint(128, 128*4)
        elif self.time == 5000:
            self.offset += 20