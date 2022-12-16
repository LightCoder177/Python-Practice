#Checking for date, time, and the day

#importing date, strftime submodules from datetime, and time modules. 

from datetime import date
from time import strftime

#dict

DateTime = dict()

DateTime['Date'] = date.isoformat(date.today())
DateTime['Time'] = strftime("%H:%M %p")
DateTime['Day'] = strftime("%A")

#Execution

print("You want to know the date, time, and the day?. The day is {0:s} and the time is {1:s}. The date is {2:s}.".format(DateTime['Day'], DateTime['Time'], DateTime['Date']))

