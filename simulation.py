#!/usr/bin/env python3

# NATIVE IMPORTS
from time import sleep, time
import random

# CONSTANTS
OUTPUT_A = 0
OUTPUT_B = 1
OUTPUT_C = 2
OUTPUT_D = 3
INPUT_1 = 0
INPUT_2 = 1
INPUT_3 = 2
INPUT_4 = 3

ROTATONS_PER_SECOND_MAX = 5  # Change to reflect how fast motors can spin

# DEFINITIONS
class LargeMotor:
    def __init__(self, output):
        self.output = output
        self.ramp_up_sp = 0
        self.ramp_down_sp = 0
        self._position = 0

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value % 360

    def on_for_rotations(self, speed_percent, rots, block=True):
        time_needed = rots / ((speed_percent / 100) * ROTATONS_PER_SECOND_MAX)

        s = "Rotating {:.2f} rotations on output {}. ETA: {:.2f} s."
        s = s.format(rots, self.output, time_needed)
        print(s)
        sleep(time_needed)
        self.position += rots*360
        print("Rotation done.")
        print("M1: {:.2f}°".format(self.position))


class MoveSteering:
    def __init__(self, output_a, output_b):
        self.output_a = output_a
        self.output_b = output_b
        self._position_a = 0
        self._position_b = 0

    @property
    def position_a(self):
        return self._position_a

    @position_a.setter
    def position_a(self, value):
        self._position_a = value % 360

    @property
    def position_b(self):
        return self._position_b

    @position_b.setter
    def position_b(self, value):
        self._position_b = value % 360

    def on_for_rotations(self, percent, speed_percent, rots, block=True):
        time_needed = rots / ((speed_percent / 100) * ROTATONS_PER_SECOND_MAX)
        motor_a_factor = 1 if percent >= 0 else (percent / 50 + 1)
        motor_b_factor = 1 if percent <= 0 else ((percent / 50)*(-1) + 1)

        s = "Rotating {:.2f} rotations on output {} and {}. ETA: {:.2f} s."
        s = s.format(rots, self.output_a, self.output_b, time_needed)
        print(s)
        sleep(time_needed)
        self.position_a += rots*360 * motor_a_factor
        self.position_b += rots*360 * motor_b_factor
        print("Rotation done.")
        print("M1: {:.2f}°, M2: {:.2f}°".format(self.position_a, self.position_b))



class TouchSensor:
    def __init__(self, input):
        self.input = input
        self._is_pressed = False

    @property
    def is_pressed(self):
        self._is_pressed = random.choice([True, False])
        return self._is_pressed

class UltrasonicSensor:
    def __init__(self, input):
        self.input = input
        self._distance_centimeters = 0

    @property
    def distance_centimeters(self):
        self._distance_centimeters = random.randint(2, 255)
        return self._distance_centimeters

class ColorSensor:
    def __init__(self, input):
        self.input = input
        self.mode = "RGB-RAW"

    def value(self):
        return random.randint(0,100)

    def value(self, ix):
        return random.randint(0,255)

class Sound:
    @staticmethod
    def play(filename):
        print("Playing", filename)
