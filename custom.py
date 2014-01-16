#!/usr/bin/python

#This is where you can set up your own scheduled by providing hour and minute when you want to start your task and duration where you say how long do you want to run it for. This is devided by each day of the week so you can run differen scheduler each day. It is possible to extend this with another column for example task and this way it can run different tasks for each setting.

week={

       'Monday':[{'hour': 10, 'minute': 19, 'duration': 460},
                 {'hour': 12, 'minute': 20, 'duration': 2},
                 {'hour': 18, 'minute': 0, 'duration': 362},
                 {'hour': 20, 'minute': 30, 'duration': 20},
                ],

       'Tuesday':[{'hour': 8, 'minute': 6, 'duration': 360},
                  {'hour': 12, 'minute': 20, 'duration': 2},
                  {'hour': 15, 'minute': 6, 'duration': 2},
                  {'hour': 21, 'minute': 38, 'duration': 360},
                 ],

       'Wednesday':[{'hour': 10, 'minute': 56, 'duration': 360},
                    {'hour': 15, 'minute': 30, 'duration': 360},
                   ],

       'Thursday':[{'hour': 8, 'minute': 30, 'duration': 360},
                   {'hour': 12, 'minute': 20, 'duration': 2},
                   {'hour': 15, 'minute': 20, 'duration': 2},
                   {'hour': 22, 'minute': 18, 'duration': 320},
                   {'hour': 23, 'minute': 14, 'duration': 1},
                  ],

	'Friday':[{'hour': 6, 'minute': 20, 'duration': 360},
                  {'hour': 9, 'minute': 10, 'duration': 362},
                  {'hour': 16, 'minute': 35, 'duration': 360},
		  {'hour': 23, 'minute': 55, 'duration': 1},
                 ],

	'Saturday':[{'hour': 11, 'minute': 44, 'duration': 1},
		    {'hour': 12, 'minute': 3, 'duration': 2},
                    {'hour': 12, 'minute': 8, 'duration': 2},
                    {'hour': 15, 'minute': 53, 'duration': 461},
                   ],

	'Sunday':[{'hour': 7, 'minute': 58, 'duration': 550},
                  {'hour': 20, 'minute': 30, 'duration': 520},
                 ]
}
