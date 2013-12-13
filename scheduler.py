from datetime import date
import datetime, time
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
oldDate = date(datetime.datetime.today().year,datetime.datetime.today().month,datetime.datetime.today().day) # year, month, day
dayofWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#day2=dayofWeek[date.weekday(oldDate)]
week={

        'Monday':[{'hour': 10, 'minute': 20, 'duration': 0},
                {'hour': 12, 'minute': 20, 'duration': 2},
                {'hour': 15, 'minute': 20, 'duration': 2},
                {'hour': 20, 'minute': 30, 'duration': 20},
                ],

        'Tuesday':[{'hour': 10, 'minute': 20, 'duration': 0},
                {'hour': 12, 'minute': 20, 'duration': 2},
                {'hour': 15, 'minute': 20, 'duration': 2},
                {'hour': 20, 'minute': 30, 'duration': 20},
                ],

        'Wednesday':[{'hour': 10, 'minute': 20, 'duration': 0},
                {'hour': 12, 'minute': 20, 'duration': 2},
                {'hour': 15, 'minute': 20, 'duration': 2},
                {'hour': 20, 'minute': 30, 'duration': 20},
                ],

        'Thursday':[{'hour': 10, 'minute': 20, 'duration': 0},
                {'hour': 12, 'minute': 20, 'duration': 2},
                {'hour': 15, 'minute': 20, 'duration': 2},
                {'hour': 20, 'minute': 30, 'duration': 20},
                ],

	'Friday':[{'hour': 10, 'minute': 20, 'duration': 0},
                {'hour': 12, 'minute': 20, 'duration': 2},
                {'hour': 15, 'minute': 36, 'duration': 1},
		{'hour': 20, 'minute': 30, 'duration': 20},
                ],

	'Saturday':[{'hour': '15:00', 'duration': 5},
		{'hour': 20, 'minute': 30, 'duration': 20},
		],

	'Sunday':[{'hour': '15:00', 'duration': 5},
                {'hour': 20, 'minute': 30, 'duration': 20},
                ]}


today = dayofWeek[date.weekday(oldDate)]
print "Today is %s in simple words it\'s %s" % (oldDate.strftime("%d%b%Y"), dayofWeek[date.weekday(oldDate)])
for s in dayofWeek:
    if s==today:
        print (s + " Winner!!")
        for instance in week[s]:
		if hour == instance['hour'] and minute == instance['minute']: 
	            print instance['hour'], instance['minute']
		    print("This is working")
		    time.sleep(instance['duration'] * 60)
		    break
