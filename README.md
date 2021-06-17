# BirdsOnBikes
## Setup
Raspberry Pi 4 + Camera Module V2

mit der Bibliothek [UV4L](https://raspberry-valley.azurewebsites.net/UV4L/), die ein einigermaßen flüssigen Videostream ermöglicht

Der Stream wird als Proxy-Server an stream.birdsh.it weitergeleitet

Der Streaming-Client befindet sich auf cam.yolobird.com

Auf dem Streaming-Client soll später auch di KI-Erkennung laufen. momentan wird dort jede Sekunde ein Standbild aus dem Stream gespeichert. Dieses Material könnte später auch genutzt werden um die KI weiter zu trainieren um später Vogelarten zu unterscheiden

mit folgendem Befehl kann das Script gestartet werden und wird auch nachdem sich der Benutzer vom Server abgemeldet hat, weiter ausgeführt

``` bash
nohup python3 getJpgFromStream.py >output.log >error.log &
```

## Installation

* Raspberry Pi OS Lite auf SD-Karte geflasht
* per SSH auf Raspberry zugreifen
* sudo apt update 
* sudo apt full-upgrade
* sudo apt install git python-picamera python3-picamera
* Kamera in raspi-config aktivieren
* git clone https://git.coco.study/mschmal2/birdsonbikes.git
* sudo shutdown now
* WLAN-Konfigurieren:
    * Speicherkarte in deinen Rechner einlegen
    * auf "boot" eine Datei mit dem Namen ``wpa_supplicant.conf`` anlegen
    * Datei im Editor öffnen und folgenden Code eingeben:

```bash ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
country=de
update_config=1
network={
    ssid="<Name of your wireless LAN>"
    psk="<Password for your wireless LAN>"
}
```

[Quelle](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md)

ssh pi@campi2 oder 3
pw: birdie

# Anleitung

## Die Komponenten

* RaspberryPi 3
<img src="assets-README/Raspi.png">
* Raspberry Kamera V.2
<img src="assets-README/Kamera.png">
* PIR Sensor (Bewegungssensor)
<img src="assets-README/PIRSensor.png">
* 3x Kabel Weiblich/ Weiblich
<img src="assets-README/Kabel.png">

## Zusammenbauen der Komponenten

    1. Den Gehäusedecke des Raspberry Pi´s abnehmen. 

    2. Das Kabel des Kamermoduls in den Beschrifteten Kamera Eingang stecken. (Hier auf die Richtung der Kontakte achten)

    3. Drei Kabel an die Pins (GND, VCC, SIG) des PIR Sensors anschließen. 

    4. Die Kabel müssen nun jeweils richtig an die Pins des Raspberry Pi´s angeschlossen werden. 
    GND = 6 / VCC = 4 / SIG = 16

<img src="assets-README/GPIO.png">

## Wifi verbindung herstellen

    1. Den Raspberry Pi ausschalten (Stromkabel entfernen)

    2. Die SD auf der Rückseite herausnehmen und in deinen Rechner einlegen

    3. Einen beliebigen Text Editor öffen (NotdePad, VS Code)

    4. Die SD Karte auswählen auf dem Ordner Boot eine neue Datei mit dem Namen: wpa_supplicant.conf anlegen

    5. Folgenden Text in die Datei kopieren:

```bash ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
country=de
update_config=1
network={
    ssid="<Name of your wireless LAN>"
    psk="<Password for your wireless LAN>"
}
```
    6. <Name of your wirless LAN> und <Password for your wireless LAN> ersetzen.

    7. Die Datei abspeichern und die SD Karte auswerfen.

    8. Die SD Karte wieder in den Raspberry Pi einlegen.

    9. Nach 5 minuten sollte sich der Raspberry Pi mit dem Internet verbunden haben
    (Um das zu überprüfen kann man per SSH auf den Raspberry Pi gehen)
    Dafür die Bash öffnen und: 

``` bash 
ssh <name des raspberry pi´s> eingeben 
```
    Namen sind in unserem Fall: 
    (pi@campi1) oder (pi@campi3)
    Das Passwort ist (birdie)





