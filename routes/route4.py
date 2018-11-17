import time 

class Route():
    def __init__(self, bot):
        self.bot = bot
        self.route_number = "four"
    
    def start(self):
        self.bot.move_forward(34, 50)
        self.bot.rotate_right(90, 50)
        self.bot.move_forward(25, 50)
        self.bot.rotate_right(90, 50)
        self.bot.move_forward(25, 50)
        time.sleep(0.5)
        self.bot.empty_container()
        self.bot.move_backward(25, 50)
        self.bot.rotate_left(90, 50)
        self.bot.move_backward(25, 50)
        self.bot.rotate_left(85, 50)
        self.bot.move_backward(34, 50)

        return True

    
