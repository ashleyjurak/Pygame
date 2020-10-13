class Settings:

    def __init__(self):
        #initialize game's static settings

        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_limit = 3
        
        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #alien settings
        self.fleet_drop_speed = 10

        #how quickly game speeds up
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        #initalize settings that change throughout the game
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #+1 is right -1 is left
        self.fleet_direction = 1 #aliens always move right at beginning of game

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self. speedup_scale