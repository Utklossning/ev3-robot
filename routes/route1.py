class Route():
    def __init__(self, bot):
        self.bot = bot
        self.route_number = "one"
    
    def start(self):
        self.bot.move_forward(56.5, 50) 
        self.bot.empty_container()
        self.bot.move_backward(56.5, 50)
        return True

    
