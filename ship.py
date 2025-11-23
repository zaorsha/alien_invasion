import pygame

class Ship:

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('assets/Spaceship.bmp')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.35,
                                                         self.image.get_height() * 0.35))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom centeer of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        self.settings = ai_game.settings

        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update the ship's position based on movement flags.
        if self.moving_right:
            if self.rect.x <= self.screen_rect.right - self.rect.width:
                self.rect.x += self.settings.ship_speed

        if self.moving_left:
            if self.rect.x >= self.screen_rect.left:
                self.rect.x -= self.settings.ship_speed
            

    def blitme(self):
        # Draw the ship at its current location.
        self.screen.blit(self.image, self.rect)