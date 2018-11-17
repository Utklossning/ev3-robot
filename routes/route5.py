import time 

class Route():
    def __init__(self, bot):
        self.bot = bot
        self.route_number = "five"
    
    def start(self):
        self.bot.move_forward(45, 50)
        self.bot.rotate_right(45, 50)
        self.bot.move_forward(36, 50)
        self.bot.rotate_right(46, 50)
        self.bot.move_forward(40, 50)
        self.bot.dectect_red_tape()
        self.bot.empty_container()
        self.bot.move_backward(40, 50)
        self.bot.rotate_left(46, 50)
        self.bot.move_backward(36, 50)
        self.bot.rotate_left(37, 50)
        self.bot.move_backward(50, 50)
    
        return True
        
        

           
        

    
