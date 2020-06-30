# Touch button.
import time
import board
import touchio
import neopixel
import digitalio
from digitalio import DriveMode

play_touch = touchio.TouchIn(board.A0)
touch_up =touchio.TouchIn(board.A2)
touch_down =touchio.TouchIn(board.A4)

play_button = digitalio.DigitalInOut(board.D13)
down_button = digitalio.DigitalInOut(board.D8)
up_button = digitalio.DigitalInOut(board.D4)

play_button.direction = digitalio.Direction.OUTPUT
down_button.direction = digitalio.Direction.OUTPUT
up_button.direction = digitalio.Direction.OUTPUT

play_button.drive_mode = DriveMode.PUSH_PULL
down_button.drive_mode = DriveMode.PUSH_PULL
up_button.drive_mode = DriveMode.PUSH_PULL

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3


while True:
    if play_touch.value:
        play_button.value = True
        led[0] = (0, 255, 0)
        print("play")
    elif touch_down.value:
        down_button.value = True
        led[0] = (255, 0, 0)
        print("down")
    elif touch_up.value:
        up_button.value = True
        led[0] = (0, 0, 255)
        print("up")
    else:
        led[0] = (0, 0, 0)
        play_button.value = False
        down_button.value = False
        up_button.value = False
    time.sleep(0.1)