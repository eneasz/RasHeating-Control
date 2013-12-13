#!/usr/bin/python
#Import stuff
import os, time, sys, glob
from datetime import datetime as t

#Temp MIN
TSET = 27
TMARG = 2
TEMP_SCALE="C" # Show temperature in C or F
#status
STATE = None

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
	elif tmp >= TSET and (STATE==False):
		print color.OKGREEN + ("Temperature " + str(tmp) + str(TEMP_SCALE) + " we don't need to runn the heating") + color.ENDC
	elif tmp<TSET and (STATE==True):
		print color.BLUE + ("Its " + str(tmp) + str(TEMP_SCALE) + " heating is running now") + color.ENDC
	elif tmp < TSET - TMARG and (STATE==None or not STATE or STATE==False):
		STATE = True
		print color.BLUE + ("Its " + str(tmp) + str(TEMP_SCALE) + " Switching ON heating") + color.ENDC
	elif TSET - TMARG <= tmp and (STATE==False or not STATE):
		print color.WARNING + ("Temperature " + str(tmp) + str(TEMP_SCALE) + " within set range, no change required") + color.ENDC

#Executing function ogrzewanie
	ogrzewanie(STATE);
	print(tmp)
	time.sleep(2)
