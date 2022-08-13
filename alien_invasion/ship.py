import pygame
from settings import Settings

class Ship:
    """Class to manage the puppy ship."""

    def __init__(self, ai_game):
        """Initialize ship and set starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('alien_invasion/images/puppy.bmp')
        self.image = pygame.transform.scale(self.image, (self.settings.puppy_width, self.settings.puppy_height))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship's position based on movement flags."""
        # Update the ship's x value, not the rect
        if self.moving_right:
            self.x += self.settings.puppy_speed
        if self.moving_left:
            self.x -= self.settings.puppy_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw ship at its current location."""

        self.screen.blit(self.image, self.rect)