#!/usr/bin/env python3

# NATIVE IMPORTS
from time import sleep
from routes.route1 import Route as route1
from routes.route2 import Route as route2
from routes.route3 import Route as route3
from routes.route4 import Route as route4
from routes.route5 import Route as route5

import bot

bot = bot.Bot(wheel_radius=2.3, wheel_spacing=15.5)

def main():
    print("Starting the main application")
    routes = [route1(bot), route2(), route3(), route4(), route5()]
    print("Loaded routes into list")
    current_route = 0
    bot.wav_processor()
    while True:
        if bot.read_touch_top():
            print("Got front key press, starting route {}".format(routes[current_route].route_number))
            bot.tts("Running route {}".format(routes[current_route].route_number))
            print("Route {} start returned: {}".format(routes[current_route].route_number, routes[current_route].start()))
        if bot.read_touch_front():
            if current_route == len(routes)-1:
                current_route = 0
            else:
                current_route += 1

            print("Got top key press, changing to route {} ".format(routes[current_route].route_number))
            bot.tts("Changed to route {}".format(routes[current_route].route_number))

    time.sleep(0.1)

if __name__ == "__main__":
    bot.tts("Booting up")
    main()
