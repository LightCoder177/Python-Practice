#Creating a program that will tell if the minute is an odd number or an even number. 

from datetime import datetime
import time
import random

Even_Number = list(range(0, 62, +2))


right_this_minute = datetime.today().minute

Random_Number = random.randint(0,10)

for repeat in range(5):
    if right_this_minute in Even_Number:
        print("This minute is an even number!!!")
    else:
        print("This minute is an odd number!")
    print(Random_Number)
    time.sleep(Random_Number)
    

