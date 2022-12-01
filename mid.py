import pygame
import random

class Mid:
    # add time dynamic and increase mids/difficulty
    # add counter at top of screen!
    # game ends if you miss catching a mid
    # menu screen? add leaderboard? option for player 2?
    # where would I add a time function?
    # add power ups?
    # how to figure out w/o copying?
    # music, sound effects, text/font!
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('images/mid.png')
        self.mid_rect = self.image.get_rect()
        self.mid_rect.x = random.randint(128, 128*4)

    def update(self):
        self.mid_rect.y += 1

    def blitme(self):
        """Draw the mid at its current location!!"""

        self.screen.blit(self.image, self.mid_rect)