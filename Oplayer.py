#!/usr/bin/env python3
import os
import time
import random
#from gpiozero import Button
import RPi.GPIO as GPIO
from signal import pause
from shutil import rmtree
import vlc

INPUT_PIN = 23
# button_play = Button(27)  # when Arduino connexion OK should be 27.
# button_shutdown = Button(17)  # Must be internal soundcard button 17.
# volume_down = Button(23)
# volume_up = Button(22)
current_dir = os.path.dirname(__file__)
medias = os.path.join(current_dir, "medias")
medias_usb = os.path.join(current_dir, "medias_usb")


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(INPUT_PIN, GPIO.IN)
    # Mount usb drive.
    os.popen(f"sudo mount -t vfat -o uid=pi,gid=pi /dev/sda2 {medias_usb}")
    remove_hidden_files()
    start_shime()
    loop()


def remove_hidden_files():
    # create media_usb folder if not exist.
    os.makedirs(medias_usb, exist_ok=True)
    # Remove '._DS_Store' hidden file in max OS in the internal /medias folder.
    path = choose_media_path()
    liste_medias = os.listdir(path)
    #liste_usb_media = os.listdir(medias_usb)
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
        if (GPIO.input(INPUT_PIN) == True):  
            o33 = o33 + 1
        if o33 == 2:
            if  (GPIO.input(INPUT_PIN) == True) and last_value == 0:
                shime()
                time.sleep(5.5)
                player = vlc.MediaPlayer(random_player())
                player.stop()
                player.play()
                last_value = 1
                time.sleep(2)
            elif (GPIO.input(INPUT_PIN) == True) and last_value == 1:
                player.stop()
                shime()
                time.sleep(5.5)
                player = vlc.MediaPlayer(random_player())
                player.play()
                last_value = 1
                time.sleep(2)
        elif o33 == 30:
            print('pause')
        else:
            if o0 == 0:
                o0 = o0 + 1
            elif o0 == 1:
                o33 = 0
                o0 = 0
        time.sleep(0.1)
        # if volume_down.is_pressed:
        #     time.sleep(0.1)
        #     os.popen("amixer -c 0 set Playback 1%-")
        # if volume_up.is_pressed:
        #     time.sleep(0.1)
        #     os.popen("amixer -c 0 set Playback 1%+")
        # if button_shutdown.is_pressed:
        #     #os.popen("sudo halt -p")
        #     os.popen("sudo reboot")
        


if __name__ == "__main__":
    try:
        print('\n\nProgram is starting...\nPress button on the PiHat to play a sound.\n')
        setup()
    except KeyboardInterrupt:
        print("Program is quitting.")
        os.system("sudo pkill vlc")
        exit()
