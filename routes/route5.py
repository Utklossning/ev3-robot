import time 

class Route():
    def __init__(self, bot):
        self.bot = bot
        self.route_number = "five"
    
    def start(self):
        self.bot.move_forward(36, 50)
        self.bot.rotate_right(90, 50)
        self.bot.move_forward(55, 50)
        self.bot.rotate_right(92, 50)
        self.bot.move_forward(19, 50)
        self.bot.detect_red_tape()
        self.bot.empty_container()

        return True

    
