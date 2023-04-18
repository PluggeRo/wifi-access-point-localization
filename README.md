# wifi-access-point-localization
Localization of a wifi access point using one single antenna

## Introduction
I have tried different approaches to receive valid and fast data from the access points:

1. Creating a gnuradio flowchart to receive the dbm value from the access point - did not work with hackrf one
2. Analyze the dbm value from the access point using a wifi adapter in monitor mode and:
- the python lib: pywifi - got valid values but really slow
- the python lib: scapy - got valid values with a frequency of around 1Hz


## Setting up the hardware
To make use of the scripts you need to make sure that your wifi adapter is in monitor mode.

### Activate monitor mode in linux
1. Start the wpa_supplicant service:
``` zsh
service wpa_supplicant start
```
2. Check the name of your wireless interface by running the command:
``` zsh
iwconfig
```
3. Bring your interface into monitor mode (e.g. for interface named `wlan0`):
``` zsh
sudo ifconfig wlan0 down && sudo iwconfig wlan0 mode monitor && sudo ifconfig wlan0 up
```

## Setting up the software
Every plugin and lib for the python script is installed in the virtual environment.
So you should be good after downloading the repo.

### Test the scapy script
1. Activate the virtual environment in VSCode:
``` zsh
py -3 -m venv .venv
.venv\scripts\activate
```
2. Execute the script in the venv:
``` zsh
sudo python analyzer_scapy.py
```
