#!/usr/bin/env python3
##################################################
# Oplayer.
# 09.06.2020 
# TODO: change button function in while true and not pause().
##################################################
import os
import time 
import random
from gpiozero import Button
from signal import pause
from shutil import rmtree
import vlc

button = Button(17)
current_dir = os.path.dirname(__file__)
medias = os.path.join(current_dir, "medias")
medias_usb = os.path.join(current_dir, "medias_usb")


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


def volume_control():
    pass


def loop():
    last_value = 0
    while True:
        if button.is_pressed and last_value == 0:
            shime()
            time.sleep(5.5)
            player = vlc.MediaPlayer(random_player())
            player.play()
            last_value = 1    
        elif button.is_pressed and last_value == 1:
            player.stop()
            shime()
            time.sleep(5.5)
            player = vlc.MediaPlayer(random_player())
            player.play()
            last_value = 0  


def setup():
    os.system(f"sudo mount -t vfat -o uid=pi,gid=pi /dev/sda2 {medias_usb}") # Mount usb drive. 
    remove_hidden_files()
    start_shime()
    loop()


if __name__ == "__main__":
    try:
        print('\n\nProgram is starting...\nPress button on the PiHat to play a sound.\n')
        setup()
    except KeyboardInterrupt:
        print("Program is quitting.")
        exit()


