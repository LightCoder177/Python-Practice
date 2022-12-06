#Saying hello to the user using his name. 

#set

First_Name = set()
Second_Name = set()

#Execution for the first name

first_name = "Ahmad"
second_name = "Mujtaba"

First_Name.add(first_name)
First_Name.add(second_name)

Name = list(sorted(First_Name))

print(''.join(Name[0]) + " " + ''.join(Name[1]))
