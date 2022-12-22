#Displaying date, time, and the day with the timezone.

#importing datetime, time, and pytz

import datetime
import time
import pytz

#dict and variable. 
KarachiTz = pytz.timezone("Asia/Karachi")
Time_In_Karachi = datetime.datetime.now(KarachiTz)
Current_time_in_karachi = Time_In_Karachi.strftime("%I:%M:%S %p")

DateTime = dict()
DateTime['Date'] = datetime.date.isoformat(datetime.date.today())
DateTime['Time'] = time.strftime("%I:%M:%S %p UTC%z")
DateTime['Day'] =  time.strftime("%A")

#Execution

print("You want to know the date, time, and the day?. Well, the date is {0:s} and the time is {1:s}. The day is {2:s}.".format(DateTime['Date'], DateTime['Time'], DateTime['Day']))
print("Current time in karachi is: ", Current_time_in_karachi)

