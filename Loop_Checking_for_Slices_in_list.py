#Creating a program that will display a message after some indentation. 

#Variable and list.

paranoid_android = "Marvin, the Paranoid Android."
letters = list(paranoid_android)

#loop and execution.

for char in letters[:6]:
    print('\t', char)
for char in letters[-8:-1]:
    print('\t'*2, char)
for char in letters[12:20]:
    print('\t'*3, char)