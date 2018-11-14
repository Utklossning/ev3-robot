#!/usr/bin/env python3

# LOCAL IMPORTS
import bot

def main():
    myBot = bot.Bot(wheel_radius=2.3, wheel_spacing=10.5)
    myBot.move_forward(distance=20, speed_percent=100)
    myBot.rotate_left(degrees=360, speed_percent=20)
    myBot.rotate_right(degrees=720, speed_percent=50)
    myBot.rotate_left(degrees=360, speed_percent=100)
    myBot.wav_processor()

if __name__ == "__main__":
    main()
