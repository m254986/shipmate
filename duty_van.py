import pygame

class Van:
    """A class to manage the van."""

    def __init__(self, ai_game):
        """Initialize the van and set its start position!"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load van img!!
        self.image = pygame.image.load('images/duty_van.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center!!
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horiz pos
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update pos based on movement flag"""
        # Update ship's x value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.van_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.van_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the van at its current location!!"""
        self.screen.blit(self.image, self.rect)