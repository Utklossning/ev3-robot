import time 

class Route():
    def __init__(self, bot):
        self.bot = bot
        self.route_number = "three"
    
    def start(self):
        self.bot.move_forward(25, 50)
        self.bot.rotate_right(46, 30)
        self.bot.move_forward(23, 50)
        time.sleep(0.5)
        self.bot.empty_container()
        self.bot.move_backward(23, 50)
        self.bot.rotate_left(35, 30)
        self.bot.move_backward(45, 75)

        return True 

    
