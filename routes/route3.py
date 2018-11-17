import time 

class Route():
    def __init__(self, bot):
        self.bot = bot
        self.route_number = "three"
    
    def start(self):
        self.bot.move_forward(50, 50)
        self.bot.rotate_right(90, 30)
        self.bot.move_forward(15, 50)
        time.sleep(0.5)
        self.bot.empty_container()
        self.bot.move_backward(15, 50)
        self.bot.rotate_left(90, 30)
        self.bot.move_backward(40, 50)

        return True 

    
