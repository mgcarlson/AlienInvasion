

class Settings:
#class to store all settings

    def __init__(self):
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 100, 180)

        #ship settings
        self.ship_speed = 5.0
        self.ship_limit = 3

        #bullet settings - dark grey bullets that are 3 pixels wide and 15 pixels high. bullets travel slower than the ship
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (25, 250, 250)
        self.bullets_allowed = 5

        #alien settings
        self.alien_speed = 2.75
        self.fleet_drop_speed = 25
        #fleet direction of 1 represents right; -1 represetns left
        self.fleet_direction = 1


