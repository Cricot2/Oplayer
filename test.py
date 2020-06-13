#!/usr/bin/env python

# Allows us to call the sleep function to slow down our loop
from time import sleep
# Allows us to call our GPIO pins and names it just GPIO
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)           # Set's GPIO pins to BCM GPIO numbering
INPUT_PIN = 23           # Sets our input pin, in this example I'm connecting our button to pin 4. Pin 0 is the SDA pin so I avoid using it for sensors/buttons
GPIO.setup(INPUT_PIN, GPIO.IN)           # Set our input pin to be an input = 0
o33 = 0
o0 = 0
# Start a loop that never ends
while True:
    if (GPIO.input(INPUT_PIN) == True):  # Physically read the pin now
        print('3.3')
        o33 = o33 + 1
        if o33 == 2:
            print('>>>>>>>>>>>>> signal')
        elif o33 == 30:
            print('pause')
        else:
            print('_')
    else:
        if o0 == 0:
            o0 = o0 + 1
        elif o0 == 1:
            o33 = 0
            o0 = 0
            print("reset")
        else:
            print("-")
    sleep(0.1);           # Sleep for a full second before restarting our loop
