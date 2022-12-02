#A shorter version of changing the meaning of word in a list. 

#list and variable. 

phrase = "Don't panic!"
plist = list(phrase)

#Executing the first phase of the program. 

print(phrase)

#Making the changes. 

new_phrase = (''.join(plist[2:0:-1]) + ''.join([plist[5], plist[6], plist[7], plist[9], plist[2]]) + ".")
print(new_phrase)