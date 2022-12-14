import sys
import pygame
import time
from random import randint

from duty_van import Duty_Van
from mid1 import Mid1
from scoreboard import Scoreboard

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((128 * 5, 128 * 4))
screen_rect = screen.get_rect()
max_offset = 128 * 4

road = pygame.image.load('images/road_asphalt22.png')
road_rect = road.get_rect()

left_road = pygame.image.load('images/road_asphalt21.png')
right_road = pygame.image.load('images/road_asphalt23.png')
grass = pygame.image.load('images/land_grass11.png')

pygame.mixer.music.load('images/hype.mp3')
pygame.mixer.music.set_volume(50)
pygame.mixer.music.play(-1)
class Shipmate:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((128 * 5, 128 * 4))
        pygame.display.set_caption("SHIPMATE!")

        self.duty_van = Duty_Van(self.screen)
        self.mid1 = Mid1(screen)
        self.scoreboard = Scoreboard(screen)

    def run_game(self):
        while True:
            # 1. check for user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Thank you for playing!!")
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.duty_van.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.duty_van.moving_left = True
                    elif event.key == pygame.K_q:
                        return False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.duty_van.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.duty_van.moving_left = False

            # 2. update game objects
            self.duty_van.update()
            if self.mid1.update(max_offset, time) == False:
                return False
            self.scoreboard.update(screen)

            # check for collision
            if self.mid1.offset >= self.duty_van.y - 1:
                if self.mid1.x >= self.duty_van.x - 23 and self.mid1.x <= self.duty_van.x + 60:
                    self.mid1.x = 1000
                    self.scoreboard.score = 1 + self.scoreboard.score
                    self.mid1.offset = 0
                    self.mid1.x = randint(128, 128 * 4)


            # 3. draw screen
            screen.blit(grass, (0, 0))
            screen.blit(grass, (0, road_rect.height))
            screen.blit(grass, (0, road_rect.height * 2))
            screen.blit(grass, (0, road_rect.height * 3))

            screen.blit(left_road, (road_rect.width, 0))
            screen.blit(left_road, (road_rect.width, road_rect.height))
            screen.blit(left_road, (road_rect.width, road_rect.height * 2))
            screen.blit(left_road, (road_rect.width, road_rect.height * 3))

            screen.blit(road, (road_rect.width * 2, 0))
            screen.blit(road, (road_rect.width * 2, road_rect.height))
            screen.blit(road, (road_rect.width * 2, road_rect.height * 2))
            screen.blit(road, (road_rect.width * 2, road_rect.height * 3))

            screen.blit(right_road, (road_rect.width * 3, 0))
            screen.blit(right_road, (road_rect.width * 3, road_rect.height))
            screen.blit(right_road, (road_rect.width * 3, road_rect.height * 2))
            screen.blit(right_road, (road_rect.width * 3, road_rect.height * 3))

            screen.blit(grass, (road_rect.width * 4, 0))
            screen.blit(grass, (road_rect.width * 4, road_rect.height))
            screen.blit(grass, (road_rect.width * 4, road_rect.height * 2))
            screen.blit(grass, (road_rect.width * 4, road_rect.height * 3))
            self.duty_van.blit(screen)
            self.mid1.blit(screen)
            self.scoreboard.blit(screen)

            pygame.display.flip()
            clock.tick(60)
            # 4. win/lose conditions
            if self.scoreboard.score == 25:
                return True

shipmate = Shipmate()
win = shipmate.run_game()
if win:
    green = (0, 255, 0)
    screen.fill(green)

else:
    red = (255, 0, 0)
    screen.fill(red)

pygame.display.flip()
time.sleep(2)
