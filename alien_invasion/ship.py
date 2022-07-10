import pygame
from settings import Settings

class Ship:
    """Class to manage the puppy ship."""

    def __init__(self, ai_game):
        """Initialize ship and set starting position."""

        self.settings = Settings()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('alien_invasion/images/puppy.bmp')
        self.image = pygame.transform.scale(self.image, (self.settings.puppy_width, self.settings.puppy_height))
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship at its current location."""

        self.screen.blit(self.image, self.rect)