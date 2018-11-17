import time

class Route():
    def __init__(self, bot):
        self.bot = bot
        self.route_number = "one"
    
    def start(self):
        self.bot.rotate_right(360, 50)
        return True

    
