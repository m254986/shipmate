import pygame

# font and music easy additions!

class Scoreboard:
    def __init__(self, screen):
        self.score = collisions
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.update()

    def update(self):
        self.score_image = self.font.render(collisions, True, self.text_color)

        self.score_rect = score.image.get_rect()
        self.score_rect.right = self.screen_rect.right - 32
        self.score_rect.top = 32

    def blit(self, screen):
        self.screen.blit(self.score_image, self.score_rect)