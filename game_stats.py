class GameStats:
    #track stats for Alien Invasion

    def __init__(self, ai_game):
        #initialize stats
        self.settings = ai_game
        self.reset_stats()

        #start alien invasion in inactive state
        self.game_active = False

    def reset_stats(self):
        #initialize stats that can change during game
        self.ships_left = self.settings.ship_limit