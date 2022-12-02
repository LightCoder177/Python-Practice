#This program will convert a string into a list and after that will conver the list into a string with a different message. 


#Creating variable. 

Phrase = "Don't panic!"
Plist = list(Phrase)

#Execution section

for repeat in range(12):
    Plist.pop()

Plist.extend(['O', 'n', ' ', 't', 'a', 'p', '.'])

New_Phrase = ''.join(Plist)
print(Phrase)
print(New_Phrase)
