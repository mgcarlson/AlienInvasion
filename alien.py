import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
#A class to represent a single alien in the fleet
    def __init__(self, ai_game):

        #Initialize the alien and set its starting position.
        super().__init__()
        self.screen = ai_game.screen 
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp') 
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):

        #Return True if alien is at edge of screen.
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        #Move the alien right or left.
        
        self.x += (self.settings.alien_speed * 
        self.settings.fleet_direction)
        self.rect.x = self.x

class GameStats:
    # Track statistics for Alien Invasion
    def __init__(self, ai_game):

        # Initialize the stats for the game 
        self.settings = ai_game.settings
        self.reset_stats()

        #Start the Alien Invasion game in an active state
        self.game_active = True

    def reset_stats(self):
        # Initialize statistics that can change during the game 
        self.ships_left = self.settings.ship_limit
        self.aliens_hit = 0

class Bullet(Sprite):
    # A class to manage bullets fired from the ship
    def __init__(self, ai_game):
        #Create a bullet object at the ship's current position #Inherit properly from Sprite by calling super method 
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        #Move the bullet up the screen
        #Update the decimal point of the bullet. 
        self.y -= self.settings.bullet_speed 

        #Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        #Draw the bullet to the screen 
        pygame.draw.rect(self.screen, self.color, self.rect)