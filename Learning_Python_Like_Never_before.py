#Changing the meaning of words in a list. 

#variable and list. 

phrase = "Don't panic!"
plist = list(phrase)

#Removing unwanted words. 

plist.remove('D')
plist.remove("'")

for repeat in range(0, 4):
    plist.pop()

#Making the changes.

plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))
plist.append(".")
new_phrase = ''.join(plist)

print(phrase)
print(new_phrase)