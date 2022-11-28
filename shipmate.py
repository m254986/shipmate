import sys
import pygame
from pygame.sprite import Sprite

pygame.init()

# how to make full screen?
# how to organize using classes and functions?
clock = pygame.time.Clock()
screen = pygame.display.set_mode((128*5,128*4))

road = pygame.image.load('images/road_asphalt22.png')
road_rect = road.get_rect()

left_road = pygame.image.load('images/road_asphalt21.png')
right_road = pygame.image.load('images/road_asphalt23.png')
grass = pygame.image.load('images/land_grass11.png')

screen.blit(grass, (0,0))
screen.blit(grass, (0, road_rect.height))
screen.blit(grass, (0, road_rect.height*2))
screen.blit(grass, (0, road_rect.height*3))

screen.blit(left_road, (road_rect.width,0))
screen.blit(left_road, (road_rect.width, road_rect.height))
screen.blit(left_road, (road_rect.width, road_rect.height*2))
screen.blit(left_road, (road_rect.width, road_rect.height*3))

screen.blit(road, (road_rect.width*2,0))
screen.blit(road, (road_rect.width*2,road_rect.height))
screen.blit(road, (road_rect.width*2, road_rect.height*2))
screen.blit(road, (road_rect.width*2, road_rect.height*3))

screen.blit(right_road, (road_rect.width*3,0))
screen.blit(right_road, (road_rect.width*3,road_rect.height))
screen.blit(right_road, (road_rect.width*3, road_rect.height*2))
screen.blit(right_road, (road_rect.width*3, road_rect.height*3))

screen.blit(grass, (road_rect.width*4,0))
screen.blit(grass, (road_rect.width*4, road_rect.height))
screen.blit(grass, (road_rect.width*4, road_rect.height*2))
screen.blit(grass, (road_rect.width*4, road_rect.height*3))

while True:
    # 1. check for user input
    # 2. update game objects
    # 3. draw screen
    # 4. win/lose conditions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Thank you for playing!!")
            sys.exit()
    pygame.display.flip()

clock.tick(60)