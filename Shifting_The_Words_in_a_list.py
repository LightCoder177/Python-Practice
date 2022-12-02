#Creating a program that will shift the words in a list and display the message in a slight different way.



#Variable and list.

paranoid_android = "Marvin, The Paranoid Android."
letters = list(paranoid_android)
new_letters = []
new_letters_two = []
new_letters_three = []

#loop and execution

for char in letters[8:11]:
    if char not in new_letters:
        new_letters.append(char)
new_letters.append(" ")

for char in letters[12:]:
    if char not in new_letters_two:
        new_letters.append(char)               #there is a mistake over but somehow i made the program worked. Can you guess what's the problem?
new_letters.pop()
letters.insert(0, letters.pop(6))

for char in letters[:7]:
    if char not in new_letters_three:
        new_letters_three.append(char)
new_letters_three.insert(1, " ")

print(paranoid_android)
print(''.join(new_letters) + ''.join(new_letters_two) + ''.join(new_letters_three))