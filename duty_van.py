import pygame

class Duty_Van:
    """A class to manage the van."""
    def __init__(self, screen):
        """Initialize the van and set its start position!"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Load van img!!
        self.image = pygame.image.load('images/duty_van2.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center!!
        self.y = 128 * 4 - 62
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horiz pos
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def blit(self, screen):
        """Draw the van at its current location!!"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update pos based on movement flag"""
        # Update ship's x value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right - 128:
            self.x += 10
        if self.moving_left and self.rect.left - 128 > 0:
            self.x -= 10

        # Update rect object from self.x
        self.rect.x = self.x