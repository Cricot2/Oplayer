# TODO:

14 juin 2020 - Après la cession avec Alex. SOIR TARD MAIS BIEN!
<br>
* Comment faire la fonction pause?? Il faut de l'assynchrone pour pouvoir faire une pause car après `o33 += 1 == 2 il y a un sleep()` pour la shime... Sinon on utilise les deux buttons de volume en combo : `if (UP + DOWN): player.pause()` en pseudo code...
* Mettre plus fort random shime.

# FIXME:
<br>
* Probleme de permition pour le player

`ALSA lib pcm\_dmix.c:1071:(snd\_pcm\_dmix\_open) unable to create IPC semaphore`

C'est un problème de permission... Le crontab est lancé en sudo et launcher appel `sudo python3 /path`
Du coup quand je lance depuis vs code depuis le terminal je perds les autorisations... Il doit y avoir un truc à faire.
