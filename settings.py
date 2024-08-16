class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #ship settings
        self.ship_limit = 3
         # Bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (30, 30, 30)
        self.bullets_allowed = 3
        # alien settings
        self.fleet_drop_speed = 10 
        # fleet_direction of 1 represents right; -1 represents left

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """Initialise settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
