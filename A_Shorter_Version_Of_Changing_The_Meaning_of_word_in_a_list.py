#Creating a program that will take 2 or 3 lines to change the meaning of a word. 

#list and variable.

phrase = "Don't panic!"
plist = list(phrase)

#Making the changes. 

new_phrase = ''.join(plist[1:3])

#Execution
print(phrase)
print(new_phrase + ''.join([plist[5],''.join(plist[4]),''.join(plist[7]),''.join(plist[6])]))