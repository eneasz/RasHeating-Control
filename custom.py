#!/usr/bin/python

#This is where you can set up your own scheduled by providing hour and minute when you want to start your task and duration where you say how long do you want to run it for. This is devided by each day of the week so you can run differen scheduler each day. It is possible to extend this with another column for example task and this way it can run different tasks for each setting.

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
                  {'hour': 17, 'minute': 34, 'duration': 1},
		  {'hour': 23, 'minute': 55, 'duration': 1},
                 ],

	'Saturday':[{'hour': 11, 'minute': 44, 'duration': 1},
		    {'hour': 12, 'minute': 3, 'duration': 2},
                    {'hour': 12, 'minute': 8, 'duration': 2},
                    {'hour': 13, 'minute': 00, 'duration': 1},
                   ],

	'Sunday':[{'hour': 15, 'minute': 44, 'duration': 5},
                  {'hour': 20, 'minute': 30, 'duration': 20},
                 ]
}
