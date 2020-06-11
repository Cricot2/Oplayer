# Oplayer

Version française. 09 juin 2020.
<br>
## Materiel :

* Raspberry pi 3.
* Sound hat WM8960-Audio-HAT (carte son). + mini HP.
* Arduino Nano.
* Carte Micro SD 16 Go.* 
* Alimentation.
* Potentiometre de volume.
* Boutton contact

## Construction :

Inclure un fichier Fritzing.

## Mode d'emploi :

### 1\_Charger de nouveaux médias dans le player:

##### Via internet :

TODO..........................................
Le player est équipé d'un server SAMBA,

##### Via une clef USB :

* La clef USB doit être formatée en MS-DOS (fat32).
* Elle doit porter le nom :  `MEDIA_USB`

#### 2\_Formater des fichiers sons :

* Préférer des fichiers ".wav" au format 24bit 48Hz pour être sur que le lecteur le prennent en compte.
* Ne pas laisser de vides trop pronancés après la fin du fichier son. 1 seconde maximum. Ne pas laisser de vide avant le fichier non plus.
* **Ne pas mettre d'espaces** dans les titres, un fichier type serait : `titre_de_mon_fichier.wav`
* Eviter les accents et autres carractères bizarres.

### 3\_Allumer le player :

Pour allumer le player il suffit de le brancher à une prise de courrant. Lorsque le player est prêt un son court est joué (il ne sera joué qu'une seule fois au démarage).

### 4\_Eteindre le player :
TODO..........................................
<br>

### 5\_Déclencher un son :

Pour allumer le player il suffit de le brancher à une prise de courrant. Lorsque le player est prêt un son court est joué (il ne sera joué qu'une seule fois au démarage).

### 4\_Eteindre le player :
TODO..........................................
<br>

# TODO

* Réglage de volume pilote Alsamixer.
* Led témoin pour le geste de délclanchement du son sur Arduino Nano.
* Documentation + Fritzing.
* Améliorer le player stop pause...
* Metttre les shime dans un dossier et créer les chemins d'accès.

# FIXME

* La clef usb ne se boot qu'une seule fois... Il faut redémarer le RPi pour y arriver. La commande est :

`sudo mount -t vfat -o uid=pi,gid=pi /dev/sda1 /media/usbhdd`

* En même temps c'est pas si génant que ça... 