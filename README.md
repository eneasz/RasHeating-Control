RasHeating-Control
==================


This is my own first little project to utilize rasberry PI to do home automation for central heating with gas boiled. In my case to switch boiler on I need to connect two pins on control panel of my boiler. To protect my rasberry I use relay which I gor of ebay.
What we'll need for this project is:
- Rasberry PI
- DS18B20 Digital Temperature Sensor 
- 4.7K Resistor


Connecting hardware
====================

Sensor I have got 3 wires: RED - Vdd, BLACK - GND, WHITE - Data
- Connect GND on the 18B20 to pin 6 (GND) on the RPi.
- Conect Data on the 18B20 to pin 7 (GPIO4) on the RPi.
- Connect  Vdd on the 18B20 to pin 1 (3V3) on the RPi.
- Put a 4.7K resistor between Data and Vdd pins on RPi.


Load the Kerne Modules
======================

sudo modprobe w1_gpio && sudo modprobe w1_therm

This will load the w1_gpio and w1_therm modules temporarily for your current session. If you reboot your Raspberry Pi, you will have to reload them. In order to load them automatically, you can add 2 lines to /etc/modules:

sudo sh -c "echo 'w1_gpio\nw1_therm\n' >> /etc/modules"


Check if your sensor is detected by the system.
=============================================

pi@raspberrypi ~ $ cat /sys/bus/w1/devices/28-00000449e4f6/w1_slave
0b 00 4b 46 7f ff 05 10 95 : crc=95 YES
0b 00 4b 46 7f ff 05 10 95 t=22583

t=22583/1000 = 22.583 <== This is Your temperature in C
