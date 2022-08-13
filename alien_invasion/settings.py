class Settings:
    """A class to store all settings for Kitten Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (120, 60, 240)

        # Puppy settings
        self.puppy_width = 105
        self.puppy_height = 128
        self.puppy_speed = 5.5