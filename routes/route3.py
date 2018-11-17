import time 

class Route():
    def __init__(self, bot):
        self.bot = bot
        self.route_number = "three"
    
    def start(self):
        self.bot.move_forward(27, 50)
        self.bot.rotate_right(45, 30)
        self.bot.move_forward(18, 50)
        time.sleep(0.5)
        self.bot.empty_container()
        self.bot.move_backward(18, 50)
        self.bot.rotate_left(35, 30)
        self.bot.move_backward(52, 50)

        return True 

    
