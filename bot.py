#!/usr/bin/env python3

RUN_SIMULATION = False  # Change to False to run on real robot.

# NATIVE IMPORTS
from math import pi

# THIRT PARTY IMPORTS
if not RUN_SIMULATION:
    from ev3dev2.motor import \
        LargeMotor, MediumMotor, MoveSteering, \
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
        self._container_motor = MediumMotor(OUTPUT_C)
        self._steering_drive = MoveSteering(OUTPUT_D, OUTPUT_A)
        self._touch_sensor_front = TouchSensor(INPUT_1)
        self._touch_sensor_top = TouchSensor(INPUT_2)
        #self._ultrasonic_sensor = UltrasonicSensor(INPUT_2)
        self._color_sensor = ColorSensor(INPUT_3)
        self._color_sensor.mode = "RGB-RAW"
        #self._color_sensor.mode = "RGB-AMBIENT"
        self._leds = Leds()
        self._sound = Sound()
        self.WHEEL_RADIUS = wheel_radius
        self.WHEEL_SPACING = wheel_spacing

    def empty_container(self):
        self._container_motor.on_for_rotations(-15, 2)

    def read_touch_front(self):
        return self._touch_sensor_front.is_pressed

    def read_touch_top(self):
        return self._touch_sensor_top.is_pressed

    def read_ultrasonic(self):
        return self._ultrasonic_sensor.distance_centimeters

    def read_color(self):
        if self._color_sensor.mode == "RGB-RAW":
            return tuple(map(self._color_sensor.value, [0,1,2]))
        elif self._color_sensor.mode == "RGB-AMBIENT":
            return self._color_sensor.value()

    def _cm_movement_to_rotations(self, distance):
        return distance / (pi*2*self.WHEEL_RADIUS) * 1.667

    def move_forward(self, distance, speed_percent, blocking=True):
        rots = self._cm_movement_to_rotations(distance)
        self._steering_drive.on_for_rotations(
            FORWARD, -speed_percent, rots, block=blocking)

    def move_backward(self, distance, speed_percent, blocking=True):
        self.move_forward(distance, -speed_percent, blocking=blocking)

    def rotate_left(self, degrees, speed_percent, blocking=True):
        distance = self.WHEEL_SPACING * pi * degrees / 360
        rots = self._cm_movement_to_rotations(distance)
        self._steering_drive.on_for_rotations(
            LEFT_ROTATION, -speed_percent, rots, block=blocking)

    def rotate_right(self, degrees, speed_percent, blocking=True):
        distance = self.WHEEL_SPACING * pi * degrees / 360
        rots = self._cm_movement_to_rotations(distance)
        self._steering_drive.on_for_rotations(
            RIGHT_ROTATION, -speed_percent, rots, block=blocking)

    def wav_processor(self):
        #self._sound.play('sounds/t2_learning_computer_x.wav')
        self._sound.play('sounds/breadcrumbs.wav')

    def tts(self, text):
        self._sound.speak(text, volume=100)

    def set_led_color(self, side, color):
        self._leds.set_color(side, color)
