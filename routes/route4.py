import time 

class Route():
    def __init__(self, bot):
        self.bot = bot
        self.route_number = "four"
    
    def start(self):
        self.bot.move_forward(45, 50)
        self.bot.rotate_right(45, 50)
        self.bot.move_forward(44, 50)
        self.bot.rotate_right(46, 50)
        self.bot.move_forward(28, 50)
        self.bot.detect_red_tape()
        self.bot.empty_container()
        self.bot.move_backward(35, 75)
        self.bot.rotate_left(46, 50)
        self.bot.move_backward(44, 75)
        self.bot.rotate_left(37, 50)
        self.bot.move_backward(57, 75)
    
        return True
        
        

           
        

    
