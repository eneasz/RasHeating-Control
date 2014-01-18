#!/usr/bin/python

#================================================================================================
#This library is is a simple script that is using an external  scheduler plan in from a dictionary in custom.py where you can define your own scheduler for each day. Library checks what day is today and if there is a scheduler for this day it will check if there is anything set up for curent time and upon match it will use a duration to determinate when task should end and run it for set duration.
#================================================================================================

#Importing stuff including scheduler-custom which is a file where you define your own scheduler
import sys, os, time, rhf
from datetime import datetime, date, timedelta

_scheduler="custom.py"
if ( not os.path.isfile(_scheduler)):
    print("Error: %s file not found" % _scheduler)
    sys.exit()
else:
    import custom

#List of Days in week
day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
RUNNING = False


while True:
#Reloading scheduler
 reload(custom)

##Setting up current time
 curently = timedelta(hours=datetime.now().hour, minutes=datetime.now().minute)

#Checking each event of Today's 
 for event in custom.week[day_of_week[date.weekday(date.today())]]:
     if RUNNING==False:
	start = timedelta(hours=event['hour'], minutes=event['minute'])
	finish = start + timedelta(minutes=event['duration'])

	if (start < curently < finish):
	    print("Running scheduler : " + str(event['hour']) + ":" + str(event['minute']) + ".00" + ". This will finish at " + str(finish))
	    RUNNING=True
	    break

#When time run out, finishing task
 if RUNNING==True:
	if curently >= finish:
            RUNNING=False
            rhf.heating_status("False")
            print("Scheduled task finished")

#Executing scheduled code when time arrived.
	if curently < finish:
#	    print("<= This is where your code gets executed at scheduler time =>")
	    STATE = rhf.run_heating(True)

 time.sleep(3)
