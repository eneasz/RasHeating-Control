#!/usr/bin/python

#================================================================================================
#This library is is a simple script that is using an external  scheduler plan in from a dictionary in custom.py where you can define your own scheduler for each day. Library checks what day is today and if there is a scheduler for this day it will check if there is anything set up for curent time and upon match it will use a duration to determinate when task should end and run it for set duration.
#================================================================================================

#Importing stuff including scheduler-custom which is a file where you define your own scheduler
import sys, os, datetime, time

_scheduler="custom.py"
if ( not os.path.isfile(_scheduler)):
    print("Error: %s file not found" % _scheduler)
    sys.exit()
else:
    import custom

#Defined dayofweek, today's date and resetting  end and skip counters
DAYOFWEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
OLDDATE = datetime.date(datetime.datetime.today().year,datetime.datetime.today().month,datetime.datetime.today().day) # year, month, day
TODAY = DAYOFWEEK[datetime.date.weekday(OLDDATE)]
END = datetime.datetime.now()
SKIP = False

while True:
#Reloading scheduler
 reload(custom)

#Setting up current time
 HOUR = datetime.datetime.now().hour
 MINUTE = datetime.datetime.now().minute

#Checking for each day of the week in search of Today
 for SCHEDULER in DAYOFWEEK:
     if SCHEDULER==TODAY and (SKIP==False or SKIP==None):
	for instance in custom.week[SCHEDULER]:
	  if (HOUR==instance['hour'] and MINUTE==instance['minute'] and SKIP==False):
            start = datetime.datetime.now()
            END = start + datetime.timedelta(minutes=instance['duration'])
	    print("Enabling scheduler : " + str(instance['hour']) + ":" + str(instance['minute']) + ". This will finish at " + str(END))
	    SKIP=True
	    break

#Executing scheduled code when time arrived.
 if datetime.datetime.now() < END and SKIP==True:
			print("<= This is where your code gets executed at scheduler time =>")
			time.sleep(2)

#When time run out, finishing task
 if datetime.datetime.now() > END and SKIP==True:
	SKIP=False
	print("Scheduled task finished")
 time.sleep(5)
