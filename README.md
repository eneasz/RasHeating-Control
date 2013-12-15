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
- Connect ANODE of LED to pin 11 (PGIO17) on RPi.
- Connect KATODE of LED with the 330R resistor
- Second leg of 330R conect with (GND)

It is possible to use multiple sensors , any aditional ona has to be in parallel with first

Load the Kerne Modules
======================
```
sudo modprobe w1_gpio && sudo modprobe w1_therm
```
This will load the w1_gpio and w1_therm modules temporarily for your current session. If you reboot your Raspberry Pi, you will have to reload them. In order to load them automatically, you can add 2 lines to /etc/modules:
```
sudo sh -c "echo 'w1_gpio\nw1_therm\n' >> /etc/modules"
```

Check if your sensor is detected by the system.
=============================================

```
eneasz@zebrapi ~/RasHeating-Control $ cat /sys/bus/w1/devices/28-*/w1_slave
68 01 4b 46 7f ff 08 10 05 : crc=05 YES
68 01 4b 46 7f ff 08 10 05 t=22500
```
t=22500/1000 = 22.5 <== This is Your temperature in C
