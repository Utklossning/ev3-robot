#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedRPS, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor, ColorSensor
from time import sleep, time

my_motor = LargeMotor(OUTPUT_A)
my_motor.ramp_up_sp = 1000 # Takes 1000 ms to ramp up speed
my_motor.ramp_down_sp = 1000 # Takes 1000 ms to ramp down speed
ts = TouchSensor(INPUT_3)
us = UltrasonicSensor(INPUT_2)
cs = ColorSensor(INPUT_4)
cs.mode = "RGB-RAW"
#cs.mode = "COL-AMBIENT"

t = time()
while True:
    dist = us.distance_centimeters
    if time()-t > 1:
        print("dist:", dist)
        print("colr:", tuple(map(cs.value, [0,1,2])))
#        print("colr:", cs.value())
        t = time()
    if ts.is_pressed:
        speed = min(max(1, 100-dist), 100)
        my_motor.on(speed)
    else:
        my_motor.stop()

'''
rots = 10
my_motor.on_for_rotations(100, rots, block=False)
print("Rotating {} times...".format(rots))

print("Motor holding:", my_motor.is_holding)

my_motor.wait(lambda state: "holding" in state)

print("Done!")
print("Stopped at position", my_motor.position)

# MoveSteering below - convenience for controlling two tires at once
sleep(3)

steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)
print("Created a MoveSteering object.")
# Rotate with a slight left turn, at a certain speed, for rots rotations
# Should use SpeedRPS but it doesn't seem to work? Crashes.
SLIGHT_LEFT = -20
steering_drive.on_for_rotations(SLIGHT_LEFT, 100, rots)
print("Reached the end.")
'''
