import time 

class Route():
    def __init__(self, bot):
        self.bot = bot
        self.route_number = "two"
    
    def start(self):
        self.bot.move_forward(34, 50)
        self.bot.rotate_right(90, 30)
        self.bot.move_forward(57, 50)
        self.bot.detect_red_tape()
        self.bot.move_forward(4, 20)
        self.bot.empty_container()
        self.bot.move_backward(60, 50)
        self.bot.rotate_left(85, 30)
        self.bot.move_backward(40, 50)
