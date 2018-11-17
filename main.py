#!/usr/bin/env python3

# NATIVE IMPORTS
from time import sleep
from routes.route1 import Route as route1

## LOCAL IMPORTS
#import bot
#
#def main():
#    myBot = bot.Bot(wheel_radius=2.3, wheel_spacing=10.5)
#    myBot.move_forward(distance=20, speed_percent=20)
#    myBot.rotate_left(degrees=360, speed_percent=50)
#    myBot.rotate_right(degrees=720, speed_percent=50)
#    myBot.rotate_left(degrees=360, speed_percent=50)
#    for i in range(100):
#        myBot.rotate_left(degrees=3.6, speed_percent=10)
#    myBot.wav_processor()
#    sleep(5)
#    print(myBot.read_touch())
#    print(myBot.read_ultrasonic())
#    print(myBot.read_color())
#

def main():
    print(route1)

if __name__ == "__main__":
    main()
