import pygame
import sys
from random import randint
from raindrop import Raindrop

# how is creating a class different?

screen = pygame.display.set_mode((400, 400))
screen_rect = screen.get_rect()
surface = pygame.surface.Surface((64, 64))
raindrop = Raindrop()
surface.fill((0, 255, 0))
clock = pygame.time.Clock()
offset = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 255))
    raindrop.draw(screen)
    raindrop.fall(400)
    pygame.display.flip()
    clock.tick(60)