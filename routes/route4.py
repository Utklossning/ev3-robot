import time 

class Route():
    def __init__(self, bot):
        self.bot = bot
        self.route_number = "four"
    
    def start(self):
        self.bot.move_forward(150, 50)
        return True

    
