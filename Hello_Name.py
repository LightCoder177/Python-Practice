#Saying hello to the user using his name. 

#variable

First_Name = input("Please type your first name here: ")

#set

Full_Name = {First_Name}

Second_Name = input("Please type your second name here: ")
Second_Name_set = {Second_Name}

if Second_Name_set in Full_Name[0]:
    print("The first name and the last name cannot be the same.") 