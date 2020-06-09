#!/usr/bin/env python3
##################################################
# Oplayer.
# 09.06.2020 
# TODO: while True pour le button. Clear pause().
# TODO: usb disque.
##################################################
import os
import time 
import random
from gpiozero import Button
from signal import pause
import vlc

button = Button(17)
current_dir = os.path.dirname(__file__)
medias = os.path.join(current_dir, "medias")


def remove_hidden_files():
    # Remove ._DS_Store hidden file in max OS in the 'medias' folder.
    liste_medias = os.listdir(medias)
    for f in liste_medias:
        if f.startswith("._"):
            os.remove(os.path.join(medias, f))


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
    randomfile = random.choice(os.listdir(medias))
    choosed_file = os.path.join(medias, randomfile)
    player = vlc.MediaPlayer(choosed_file)
    player.play()


def volume_control():
    pass


def onButton_pressed():
    shime()
    time.sleep(5.5)
    random_player()


if __name__ == "__main__":
    try:
        print('\n\nProgram is starting...\nPress button on the PiHat to play a sound.')
        button.when_pressed = onButton_pressed
        remove_hidden_files()
        start_shime()
    except KeyboardInterrupt:
        print("Program is quitting.")
        exit()

pause()
