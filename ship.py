import pygame

class Ship:
    #class to manage the ship

    def __init__(self, ai_game):
        #initializs the ship and set its tsarting position

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and gets its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom of the center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal value for the ship's horizonatal posiiton
        self.x = float(self.rect.x)

        #movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update teh ship's position based on the movement flags
        #update the ship's x value, not the rect. Make sure ship will remain in field view of the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:    
            self.x -= self.settings.ship_speed
        
        #Update the rect object from self x
        self.rect.x = self.x

    def blitme(self):
        #draw the ship
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        #center the ship
        self.rect.midbottom = self.screen_rect.midbottom
        