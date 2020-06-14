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
    GPIO.setup(touch_play, GPIO.IN)
    GPIO.setup(button_shutdown, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(touch_vol_down, GPIO.IN)
    GPIO.setup(touch_vol_up, GPIO.IN)
    # Mount usb drive.
    # os.popen(f"sudo mount -t vfat -o uid=pi,gid=pi /dev/sda2 {medias_usb}")
    remove_hidden_files()
    start_shime()
    loop()


def remove_hidden_files():
    # create media_usb folder if not exist.
    os.makedirs(medias_usb, exist_ok=True)
    # Remove '._DS_Store' hidden file in max OS in the internal /medias folder.
    path = choose_media_path()
    liste_medias = os.listdir(path)
    # liste_usb_media = os.listdir(medias_usb)
    for f in liste_medias:
        if f.startswith("._"):
            os.remove(os.path.join(path, f))
        elif f.startswith("."):
            rmtree(os.path.join(path, f))


def choose_media_path():
    list_usb = os.listdir(medias_usb)
    if list_usb:
        return medias_usb
    else:
        return medias


def start_shime():
    # Just for say player is ready when powered.
    path_to_shime = os.path.join(current_dir, 'start_shime.wav')
    shime_player = vlc.MediaPlayer(path_to_shime)
    shime_player.play()


def shime():
    # Sound played before the random selected cue.
    path_to_shime = os.path.join(current_dir, 'random_shime.wav')
    shime_player = vlc.MediaPlayer(path_to_shime)
    shime_player.play()


def random_player():
    randomfile = random.choice(os.listdir(choose_media_path()))
    choosed_file = os.path.join(choose_media_path(), randomfile)
    return choosed_file


def loop():
    last_value = 0
    o33 = 0
    o0 = 0
    while True:
        if (GPIO.input(touch_play) == True):  # Physically read the pin now
            o33 = o33 + 1
            if o33 == 2:
                if (GPIO.input(touch_play) == True) and last_value == 0:
                    print("if 1")
                    shime()
                    time.sleep(5.5)
                    player = vlc.MediaPlayer(random_player())
                    player.stop()
                    player.play()
                    last_value = 1
                    time.sleep(2)
                elif (GPIO.input(touch_play) == True) and last_value == 1:
                    print("if 2")
                    player.stop()
                    shime()
                    time.sleep(5.5)
                    player = vlc.MediaPlayer(random_player())
                    player.play()
                    last_value = 1
                    time.sleep(2)
            elif o33 == 15:
                print('pause')
                player.pause()
                last_value = 0
                o33 = 0
                o0 = 0
                time.sleep(3)
        else:
            if o0 == 0:
                o0 = o0 + 1
            elif o0 == 1:
                o33 = 0
                o0 = 0
        if (GPIO.input(touch_vol_down) == True):
            print("volume_down")
            time.sleep(0.1)
            os.popen("amixer -c 0 set Playback 1%-")
        if (GPIO.input(touch_vol_up) == True):
            print("volume_up")
            time.sleep(0.1)
            os.popen("amixer -c 0 set Playback 1%+")
        if (GPIO.input(button_shutdown) == GPIO.LOW):  
            print("SHUTDOWN")
            time.sleep(1)
            os.popen("sudo halt -p")
    time.sleep(0.1)    


if __name__ == "__main__":
    try:
        print('\n\nProgram is starting...\nPress button on the PiHat to play a sound.\n')
        setup()
    except KeyboardInterrupt:
        print("Program is quitting.")
        os.system("sudo pkill vlc")
        exit()
