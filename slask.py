#!/usr/bin/env python3

# Plug a touch sensor into any sensor port
from ev3dev.ev3 import *
ts = TouchSensor()

while True:
    Leds.set_color(Leds.LEFT, (Leds.GREEN, Leds.RED)[ts.value()])