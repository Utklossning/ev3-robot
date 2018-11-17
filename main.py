#!/usr/bin/env python3

# NATIVE IMPORTS
from time import sleep
from routes.route1 import Route as route1
from routes.route2 import Route as route2
from routes.route3 import Route as route3
from routes.route4 import Route as route4
from routes.route5 import Route as route5

import bot

def main():
    routes = [route1, route2, route3, route4, route5]
    current_route = 0
    while True:
        if bot.read_touch_front():
            routes[current_route].start()
        if bot.read_touch_top():
            if current_route == len(routes):
                current_route = 0
            else:
                current_route += 1

    time.sleep(0.1)

if __name__ == "__main__":
    bot.wav_processor()
    main()

