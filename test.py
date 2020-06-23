import os
import time
import random
import RPi.GPIO as GPIO
from shutil import rmtree
import vlc

touch_play = 23
button_shutdown = 17
touch_vol_down = 6
touch_vol_up = 16

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(touch_play, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button_shutdown, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(touch_vol_down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(touch_vol_up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    main()

def vol_down():
    print("volume_down")
    time.sleep(0.1)


def vol_up():
    print("volume_up")
    time.sleep(0.1)


def shutdown():
    print("SHUTDOWN")


def main():
    while True:
        if (GPIO.input(touch_play) == GPIO.HIGH):
            print("play")
            time.sleep(0.1)
        if (GPIO.input(touch_vol_down) == GPIO.HIGH):
            vol_down()
        if (GPIO.input(touch_vol_up) == GPIO.HIGH):
            vol_up()
        if (GPIO.input(button_shutdown) == GPIO.LOW):
            shutdown()
    time.sleep(0.1)

setup()