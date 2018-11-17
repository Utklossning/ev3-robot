import time 

class Route():
    def __init__(self, bot):
        self.bot = bot
        self.route_number = "four"
    
    def start(self):
        self.bot.move_forward(34, 50)
        self.bot.rotate_right(90, 50)
        self.bot.move_forward(55, 50)
        self.bot.rotate_right(90, 50)
        self.bot.move_forward(35, 50)
        time.sleep(0.5)
        self.bot.empty_container()
        self.bot.move_backward(35, 50)
        self.bot.rotate_left(90, 50)
        self.bot.move_backward(55, 50)
        self.bot.rotate_left(80, 50)
        self.bot.move_backward(34, 50)

        return True

    
