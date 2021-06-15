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
    * auf "boot" eine Datei mit dem Namen ``wpa_supplicant.conf``anlegen
    * Datei im Editor öffnen und folgenden Code eingeben:

```bash ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
country=de
update_config=1
network={
    ssid="<Name of your wireless LAN>"
    psk="<Password for your wireless LAN>"
}
```

