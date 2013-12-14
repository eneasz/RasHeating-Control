#!/usr/bin/python

#Importing stuff including scheduler-custom which is a file where you define your own scheduler
import custom, datetime, time

#Defined dayofweek, today's date and resetting  end and skip counters
dayofWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
oldDate = datetime.date(datetime.datetime.today().year,datetime.datetime.today().month,datetime.datetime.today().day) # year, month, day
today = dayofWeek[datetime.date.weekday(oldDate)]
end = datetime.datetime.now()
skip = False

while True:
#Reloading scheduler and setting curent time
 reload(custom)
 import custom
 hour = datetime.datetime.now().hour
 minute = datetime.datetime.now().minute

#Checking for each day of the week in search of Today
 for s in dayofWeek:
     if s==today and (skip==False or skip==None):
	for instance in custom.week[s]:
	  if (hour==instance['hour'] and minute==instance['minute'] and skip==False):
            start = datetime.datetime.now()
            end = start + datetime.timedelta(minutes=instance['duration'])
	    print("Enabling scheduler : " + str(instance['hour']) + ":" + str(instance['minute']) + ". This will finish at " + str(end))
	    skip=True
	    break

#Executing scheduled code when time arrived.
 if datetime.datetime.now() < end and skip==True:
			print("<= This is where your code gets executed at scheduler time =>")
			time.sleep(2)

#When time run out, finishing task
 if datetime.datetime.now() > end and skip==True:
	skip=False
	print("Scheduled task finished")
 time.sleep(5)
