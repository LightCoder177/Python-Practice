#Checking if the hour and the minute are odd or even numbers.

#importing datetime, randint, and sleep submodules from datetime, random, and time modules.

from datetime import datetime
from random import randint
from time import sleep

#list, dict, and variable. 

odd = list(range(1, 60, 2))

Time_Info = {'Hour': datetime.today().hour,
             'Minute': datetime.today().minute}

random_number = randint(1, 5)

#loop, condition, and execution

for repeat in range(1, 5):
    if (Time_Info['Hour'] in odd 
        and Time_Info['Minute'] in odd):
        print("This hour and minute are odd, don't you think?")
    else:
        print("This hour or minute is even, which is not odd.")
    sleep(random_number)