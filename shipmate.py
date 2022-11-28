import sys
import pygame

from duty_van import Van
from settings import Settings
from interface import Interface

# how to organize using classes and functions?
clock = pygame.time.Clock()

class Shipmate:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((128 * 5, 128 * 4))
        pygame.display.set_caption("SHIPMATE!")

        self.van = Van(self)

    def run_game(self):
        while True:
            # 1. check for user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Thank you for playing!!")
                    sys.exit()
            # 2. update game objects
            self.van.update()
            # 3. draw screen
            screen = pygame.display.set_mode((128 * 5, 128 * 4))

            road = pygame.image.load('images/road_asphalt22.png')
            road_rect = road.get_rect()

            left_road = pygame.image.load('images/road_asphalt21.png')
            right_road = pygame.image.load('images/road_asphalt23.png')
            grass = pygame.image.load('images/land_grass11.png')

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
            self.van.blitme()
            pygame.display.flip()
            # 4. win/lose conditions

if __name__ == '__main__':
    # Make a game instance then run da game!!
    ai = Shipmate()
    ai.run_game()

clock.tick(60)