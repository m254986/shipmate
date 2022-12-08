import pygame

class Scoreboard:
    def __init__(self, screen):
        self.score = 0
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('Impact', 25)

    def update(self,screen):
        self.score_image = self.font.render(f"Score: {self.score}", True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 32
        self.score_rect.top = 32

    def blit(self, screen):
        self.screen.blit(self.score_image, self.score_rect)