#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedRPS, MoveSteering
from time import sleep

my_motor = LargeMotor(OUTPUT_A)
my_motor.ramp_up_sp = 1000 # Takes 1000 ms to ramp up speed
my_motor.ramp_down_sp = 1000 # Takes 1000 ms to ramp down speed

rots = 10
my_motor.on_for_rotations(SpeedRPS(0.5), rots)
print("Rotating {} times...".format(rots))

my_motor.wait_until_not_moving()
print("Done!")
print("Stopped at position", my_motor.position)

# MoveSteering below - convenience for controlling two tires at once
del(my_motor)
sleep(3)

steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

# Rotate with a slight left turn, at a certain speed, for rots rotations
SLIGHT_LEFT = -20
steering_drive.on_for_rotations(SLIGHT_LEFT, SpeedRPS(0.5), rots)