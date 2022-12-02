#book solution to the problem
#This program will convert a string into a list and after that will convert the list into a string with a different message. 


#Creating variable. 

Phrase = "Don't panic!"
Plist = list(Phrase)

#Execution section

for repeat in range(4):
    Plist.pop()
Plist.pop(0)
Plist.remove("'")
Plist.extend([Plist.pop(), Plist.pop()])
Plist.insert(2, Plist.pop(3))

New_Phrase = ''.join(Plist)
print(Phrase)
print(New_Phrase)