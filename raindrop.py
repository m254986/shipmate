import pygame
import sys
from random import randint

screen = pygame.display.set_mode((400, 400))
surface = pygame.surface.Surface((64, 64))
picture = pygame.image.load('images/arrow_yellow.png')
surface.fill((0, 255, 0))
clock = pygame.time.Clock()
offset = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 255))
    screen.blit(surface, (200, 200 + offset))
    screen.blit(surface, (100, 245 + offset))
    screen.blit(picture, (125, 64 + offset))
    offset = offset + 1

    pygame.display.flip()
    clock.tick(60)