import time 

class Route():
    def __init__(self, bot):
        self.bot = bot
        self.route_number = "two"
    
    def start(self):
        self.bot.move_forward(34, 50)
        self.bot.rotate_right(87, 30)
        self.bot.move_forward(57, 50)
        self.bot.detect_red_tape()
        self.bot.move_forward(3, 20)
        self.bot.empty_container()
        self.bot.move_backward(65, 75)
        self.bot.rotate_left(85, 30)
        self.bot.move_backward(52, 75)
        
        return True
