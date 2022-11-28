class Settings:
    """A class to store all settings for SHIPMATE!."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 128*5
        self.screen_height = 128*4
        self.bg_color = (0, 0, 0)

        # van settings
        self.van_speed = 1.5