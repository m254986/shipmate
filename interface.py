import pygame
from pygame.sprite import Sprite

class Interface(Sprite):

    def __init__(self, position):
        super().__init__()
        self.image = pygame.surface.Surface((128, 128))

        # idk here
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

    def draw(self, surface):
        surface.blit(self.image, self.rect)