#!/usr/bin/env python3

RUN_SIMULATION = False  # Change to False to run on real robot.

# NATIVE IMPORTS
from math import pi

# THIRT PARTY IMPORTS
if not RUN_SIMULATION:
    from ev3dev2.motor import \
        LargeMotor, MoveSteering, \
        OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
    from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
    from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor, ColorSensor
    from ev3dev2.sound import Sound
    from ev3dev2.led import Leds

# LOCAL IMPORTS
if RUN_SIMULATION:
    from simulation import *

# CONSTANTS
FORWARD = 0
LEFT_ROTATION = -100
RIGHT_ROTATION = 100

# DEFINITIONS
class Bot:
    def __init__(self, wheel_radius, wheel_spacing):
        #self._grip_motor = self._init_motor(OUTPUT_C)
        #self._arm_motor = self._init_motor(OUTPUT_D)
        self._steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)
        self._touch_sensor = TouchSensor(INPUT_1)
        self._ultrasonic_sensor = UltrasonicSensor(INPUT_2)
        self._color_sensor = ColorSensor(INPUT_3)
        self._color_sensor.mode = "RGB-RAW"
        #self._color_sensor.mode = "RGB-AMBIENT"
        self._leds = Leds()
        self.WHEEL_RADIUS = wheel_radius
        self.WHEEL_SPACING = wheel_spacing

    def _init_motor(self, output):
        m = LargeMotor(output)
        m.ramp_up_sp = 1000
        m.ramp_down_sp = 1000
        return m

    def read_touch(self):
        return self._touch_sensor.is_pressed

    def read_ultrasonic(self):
        return self._ultrasonic_sensor.distance_centimeters

    def read_color(self):
        if self._color_sensor.mode == "RGB-RAW":
            return tuple(map(self._color_sensor.value, [0,1,2]))
        elif self._color_sensor.mode == "RGB-AMBIENT":
            return self._color_sensor.value()

    def _cm_movement_to_rotations(self, distance):
        return distance / (pi*2*self.WHEEL_RADIUS)

    def move_forward(self, distance, speed_percent, blocking=True):
        rots = self._cm_movement_to_rotations(distance)
        self._steering_drive.on_for_rotations(
            FORWARD, speed_percent, rots, block=blocking)

    def rotate_left(self, degrees, speed_percent, blocking=True):
        distance = self.WHEEL_SPACING * pi * degrees / 360
        rots = self._cm_movement_to_rotations(distance)
        self._steering_drive.on_for_rotations(
            LEFT_ROTATION, speed_percent, rots, block=blocking)

    def rotate_right(self, degrees, speed_percent, blocking=True):
        distance = self.WHEEL_SPACING * pi * degrees / 360
        rots = self._cm_movement_to_rotations(distance)
        self._steering_drive.on_for_rotations(
            RIGHT_ROTATION, speed_percent, rots, block=blocking)

    def wav_processor(self):
        Sound.play('t2_learning_computer_x.wav')

    def set_led_color(self, side, color):
        self._leds.set_color(side, color)
