#!/usr/bin/env python3
import os
import time
import random
import RPi.GPIO as GPIO
from shutil import rmtree
import vlc

touch_play = 23
button_shutdown = 17
touch_vol_down = 24
touch_vol_up = 25
current_dir = os.path.dirname(__file__)
medias = os.path.join(current_dir, "medias")
medias_usb = os.path.join(current_dir, "medias_usb")


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(touch_play, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button_shutdown, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(touch_vol_down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(touch_vol_up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # Mount usb drive.
    os.popen(f"sudo mount -t vfat -o uid=pi,gid=pi /dev/sda2 {medias_usb}")
    start_shime()
    remove_hidden_files()
    main()


def vol_down():
    print("volume_down")
    time.sleep(0.1)
    os.popen("amixer -c 0 set Playback 1%-")


def vol_up():
    print("volume_up")
    time.sleep(0.1)
    os.popen("amixer -c 0 set Playback 1%+")


def shutdown():
    print("SHUTDOWN")
    os.popen("sudo halt -p")


def remove_hidden_files():
    """Create media_usb folder if not exist."""
    os.makedirs(medias_usb, exist_ok=True)
    """Remove '._DS_Store' hidden file in max OS in the internal /medias folder."""
    path = choose_media_path()
    time.sleep(0.1)
    liste_medias = os.listdir(path)
    for f in liste_medias:
        if f.startswith("._"):
            os.remove(os.path.join(path, f))
        elif f.startswith("."):
            rmtree(os.path.join(path, f), ignore_errors=True)


def choose_media_path():
    list_usb = os.listdir(medias_usb)
    if list_usb:
        return medias_usb
    else:
        return medias


def start_shime():
    # Just for say player is ready when powered.
    path_to_shime = os.path.join(current_dir, "shimes", "start_shime.wav")
    shime_player = vlc.MediaPlayer(path_to_shime)
    shime_player.play()


def shime():
    # Sound played before the random selected cue. Wait uuntil end of file.
    path_to_shime = os.path.join(current_dir, "shimes", "random_shime.wav")
    shime_player = vlc.MediaPlayer(path_to_shime)
    shime_player.play()
    time.sleep(1.5)
    duration = shime_player.get_length() / 1000
    time.sleep(duration - 0.5)


def random_file_select(is_playing=""):
    randomfile = random.choice(os.listdir(choose_media_path()))
    choosed_file = os.path.join(choose_media_path(), randomfile)
    if choosed_file != is_playing:
        return choosed_file
    else: 
        randomfile = random.choice(os.listdir(choose_media_path()))
        choosed_file = os.path.join(choose_media_path(), randomfile)
        return choosed_file


def main():
    last_value = 0
    while True:
        if (GPIO.input(touch_play) == GPIO.HIGH) and last_value == 0:
            shime()
            choosed_file = random_file_select()
            is_playing = choosed_file
            player = vlc.MediaPlayer(choosed_file)
            player.play()
            last_value = 1
            time.sleep(2)
        elif (GPIO.input(touch_play) == GPIO.HIGH) and last_value == 1:
            player.stop()
            time.sleep(0.1)
            shime()
            choosed_file = random_file_select(is_playing)
            is_playing = choosed_file
            player = vlc.MediaPlayer(choosed_file)
            player.play()
            last_value = 1
            time.sleep(2)
        # if (GPIO.input(touch_vol_down) == GPIO.HIGH):
        #     vol_down()
        # if (GPIO.input(touch_vol_up) == GPIO.HIGH):
        #     vol_up()
        if (GPIO.input(button_shutdown) == GPIO.LOW):
            player.stop()
            #shutdown()
    time.sleep(0.1)


try:
    print('\n\nProgram is starting...\nPress button on the PiHat to play a sound.\n')
    setup()
except KeyboardInterrupt:
    print("Program is quitting.")
    exit()
except Exception:
    print("unknown error")
    setup()
