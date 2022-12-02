#Creating a program that will tell if the hour is an even or odd and the minute.

#calling the right for this job. 

from datetime import datetime
from random import randint
from time import sleep

#list and variable.

odd = list(range(1, 60, 2))

right_this_hour = datetime.today().hour
right_this_minute = datetime.today().minute

random_number = randint(1, 5)

#Loop and execution. 

for repeat in range(0, 5):
    if right_this_hour or right_this_minute in odd:
        print("This hour or minute is an odd.")
    else:
        print("This hour or minute is an even. Not an odd.")
    sleep(random_number)