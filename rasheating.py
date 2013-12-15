#!/usr/bin/python
#Import stuff
import os, time, sys, glob
from datetime import datetime as t
import RPi.GPIO as GPIO ## Import GPIO library

#Checking if we already are root and if not reloading with sudo.
#Thanks to https://gist.github.com/davejamesmiller/1965559
if os.geteuid() != 0:
	os.execvp("sudo", ["sudo"] + sys.argv)

#Setting GPIO controling LED - ON  when heating is running, OFF when it's not running
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(11, GPIO.OUT) ## Setup GPIO Pin 11 to OUT

TSET = 19.5 #Tempe max 
TMARG = 1 # TSET - TMARG = Minimal temperature below which heating will be enabled
TEMP_SCALE="C" # Show temperature in C or F
STATE = None # Reseting status
LED=True # Set to True or False to enable or disable LED

if LED==True:
	SPEED = 0.2 #Speed how quickly LED is blinking
	NUMTIMES = 4 #How many time blink in each sequence

	def Blink(speed):
		for i in range(0,NUMTIMES):## Run loop NUMTIMES
       	         GPIO.output(11,True)## Switch on pin 11
       	         time.sleep(speed)## Wait
       	         GPIO.output(11,False)## Switch off pin 11
       	         time.sleep(speed)## Wait

#Set sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

#Def reading temperature  as raw
def read_temp_raw():
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

#Def read temperature with nice conversation
def read_temp():
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp = float(temp_string) / 1000.0
		if TEMP_SCALE is 'F' :
                	temp = temp * 9.000 / 5.000 + 32.000
                return temp

if not os.geteuid() == 0:
        sys.exit('Script must run as root')

#Colors definition
class color:
    HEADER = '\033[97m'
    BLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

#Starting loop
while True:

	hour = t.now().hour
	minute = t.now().minute


#Clear screen
	os.system('clear')

#Display parameters
	print color.HEADER + ( "Settings:\n" + "Time : " + str(hour) + ":" + str(minute) + "\n" + "Temperature min: " + str(TSET - TMARG) + str(TEMP_SCALE) + "\n" + "Temperature max: " + str(TSET) + str(TEMP_SCALE) + "\n") + color.ENDC

#Define action
	def ogrzewanie(STATE):
		if STATE!=False and STATE!=True :
			STATE=False
		print(STATE)

#Reading curent temperature and making sure it's a number
	tmp = read_temp()
	try:
		int(tmp)
	except:
		print color.FAIL + ("Temperature value is not a number") + color.ENDC
		ogrzewanie("OFF")
		break


#Making decision weather to switch on/off
	if tmp >= TSET and (STATE==None or STATE==True):
		STATE = False
		print color.OKGREEN + ("Temperature " + str(tmp) + str(TEMP_SCALE) + " reached MAX, switching OFF heating") + color.ENDC
		if LED==True: GPIO.output(11,False) ## Turn on GPIO pin 11
	elif tmp >= TSET and (STATE==False):
		print color.OKGREEN + ("Temperature " + str(tmp) + str(TEMP_SCALE) + " we don't need to runn the heating") + color.ENDC
		if LED==True: GPIO.output(11,False) ## Turn on GPIO pin 11
	elif tmp<TSET and (STATE==True):
		print color.BLUE + ("Its " + str(tmp) + str(TEMP_SCALE) + " heating is running now") + color.ENDC
		if LED==True: Blink(float(SPEED))
	elif tmp < TSET - TMARG and (STATE==None or not STATE or STATE==False):
		STATE = True
		print color.BLUE + ("Its " + str(tmp) + str(TEMP_SCALE) + " Switching ON heating") + color.ENDC
		if LED==True: Blink(float(SPEED))
	elif TSET - TMARG <= tmp and (STATE==False or not STATE):
		print color.WARNING + ("Temperature " + str(tmp) + str(TEMP_SCALE) + " within set range, no change required") + color.ENDC
		if LED==True: GPIO.output(11,False) ## Turn off GPIO pin 11

#Executing function ogrzewanie
	ogrzewanie(STATE);
	print(tmp)
	time.sleep(1)
