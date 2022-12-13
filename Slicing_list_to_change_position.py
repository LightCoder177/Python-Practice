#Slicing list again to change the position of the words. 

#variable and list. 

paranoid_android = "Marvin, The Paranoid Android."
letter = list(paranoid_android)

Paranoid_Android = ''.join(letter[8:11]) + ''.join(letter[11:21]) + ''.join(letter[-8:-1:1]) + ''.join(letter[6]) + ''.join(letter[7]) + ''.join(letter[:6]) + ''.join(letter[-1])

print(paranoid_android)
print(Paranoid_Android)