#!/usr/bin/env python3

# NATIVE IMPORTS
from time import sleep
from routes.route1 import Route as route1
from routes.route2 import Route as route2
from routes.route3 import Route as route3
from routes.route4 import Route as route4
from routes.route5 import Route as route5
from routes.route6 import Route as route6

import bot

bot = bot.Bot(wheel_radius=2.74, wheel_spacing=18)

def main():
    print("Starting the main application")
    routes = [route1(bot), route2(bot), route3(bot), route4(bot), route5(bot), route6(bot)]
    print("Loaded routes into list")
    current_route = 0
    bot.wav_processor()
    while True:
        if bot.read_touch_top():
            print("Got front key press, starting route {}".format(routes[current_route].route_number))
            bot.tts("{}".format(routes[current_route].route_number))
            line_found = False
            while not line_found:
                bot.move_forward(1, 5, blocking=False)
                sens = bot.read_color()
                if sens < 30:
                    line_found = True
                    bot.stop()
            print("Route {} start returned: {}".format(routes[current_route].route_number, routes[current_route].start()))
        if bot.read_touch_front():
            if current_route == len(routes)-1:
                current_route = 0
            else:
                current_route += 1

            print("Got top key press, changing to route {} ".format(routes[current_route].route_number))
            bot.tts("{}".format(routes[current_route].route_number))

    time.sleep(0.1)

if __name__ == "__main__":
    main()
