RasHeating-Control
==================


This is my own first little project to utilize a RasberryPi to do home automation for a gas central heating boiler. In my case, to switch the boiler on I need to connect two pins on the control panel of my boiler. To protect my RasberryPi, i'll use relay which I got off of ebay.
What we'll need for this project is:
- Rasberry PI
- DS18B20 Digital Temperature Sensor 
- 4.7K Resistor
- Relay (TBD)


Connecting Hardware
====================

The DS18B20 Temperature Sensor I have has got 3 wires: RED - VDD, BLACK - GND, WHITE - Data/GPIO
- Connect GND on the DS18B20 to pin 6 (GND) on the RPi.
- Conect Data on the DS18B20 to pin 7 (GPIO4) on the RPi.
- Connect  Vdd on the DS18B20 to pin 1 (3V3) on the RPi.
- Put a 4.7K resistor between Data and Vdd pins on RPi (This pulls the I2C bus voltage up).
- Connect ANODE of LED to pin 11 (GIO17) on RPi.
- Connect CATHODE of LED with the 330 ohm resistor
- Second leg of 330 ohm resistor connects to (GND)

It is possible to use multiple sensors; any aditional ones have to be in parallel with first (additional resistors are NOT required).

Load the Kernel Modules
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
$ cat /sys/bus/w1/devices/28-*/w1_slave
68 01 4b 46 7f ff 08 10 05 : crc=05 YES
68 01 4b 46 7f ff 08 10 05 t=22500
```
t=22500/1000 = 22.5 <== This is Your temperature in C

Checking out this repository
============================
To check out the code from this repository, simply do:

```
sudo apt-get install git
git clone https://github.com/eneasz/RasHeating-Control
cd RasHeating-Control
```

You can then start the script/scheduler by calling:

```
./scheduler
```

You can manage the Time Periods in which you want to run, by amending the contents of ```custom.py```.
