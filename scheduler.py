#!/usr/bin/python

#Importing stuff including scheduler-custom which is a file where you define your own scheduler
#sys.path.append('/Users/eneasz/python/RasHeating-Control')
from datetime import date
import custom
import datetime, time

#Define how to find out hour, minute and day of the week
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
dayofWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
oldDate = date(datetime.datetime.today().year,datetime.datetime.today().month,datetime.datetime.today().day) # year, month, day
today = dayofWeek[date.weekday(oldDate)]


print "Today is %s %s" % (dayofWeek[date.weekday(oldDate)], (oldDate.strftime("%d%b%Y")))
for s in dayofWeek:
    if s==today:
        print (s + " Winner!!")
        for instance in custom.week[s]:
		if hour == instance['hour'] and minute == instance['minute']: 
	            print instance['hour'], instance['minute']
		    print("This is working")
		    time.sleep(instance['duration'] * 60)
		    break
