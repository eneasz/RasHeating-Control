#!/usr/bin/python
#Import stuff
import os, time, sys, glob
from datetime import datetime as t

#Temp MIN
tmarg = "2"
tmarg = int(tmarg)


#Temp set
tset = "27"
tset = int(tset)

#status
state = None

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
                temp_c = float(temp_string) / 1000.0
               # temp_f = temp_c * 9.000 / 5.000 + 32.000
                return temp_c

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
	print color.HEADER + ( "Settings:\n" + "Time : " + str(hour) + ":" + str(minute) + "\n" + "Temperature min: " + str(tset - tmarg) + "C\n" + "Temperature max: " + str(tset) + "C\n") + color.ENDC

#Define action
	def ogrzewanie(state):
		if state!=False and state!=True :
			state=False
		print(state)

#Reading curent temperature and making sure it's a number
	tmp = read_temp()
	try:
		int(tmp)
	except:
		print color.FAIL + ("Temperature value is not a number") + color.ENDC
		ogrzewanie("OFF")
		break
	tmp = int(tmp)


#Making decision weather to switch on/off
	if tmp >= tset and (state==None or state==True):
		state = False
		print color.OKGREEN + ("Temperature " + str(tmp) + " reached MAX, switching OFF heating") + color.ENDC
	elif tmp >= tset and (state==False):
		print color.OKGREEN + ("Temperature " + str(tmp) + " we don't need to runn the heating") + color.ENDC
	elif tmp<tset and (state==True):
		print color.BLUE + ("Its " + str(tmp) + "C heating is running now") + color.ENDC
	elif tmp < tset - tmarg and (state==None or not state or state==False):
		state = True
		print color.BLUE + ("Its " + str(tmp) + "C Switching ON heating") + color.ENDC
	elif tset - tmarg <= tmp and (state==False or not state):
		print color.WARNING + ("Temperature " + str(tmp) + "C within set range, no change required") + color.ENDC

#Executing function ogrzewanie
	ogrzewanie(state);
	print(tmp)
	time.sleep(2)
