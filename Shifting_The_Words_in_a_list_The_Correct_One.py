#Changing the position of words in a list. 

#Variable and list.

paranoid_android = "Marvin, The Paranoid Android."
first_word = []
second_word = []
third_word = []
fourth_word = []

letters = list(paranoid_android)

#Loop and execution.

for char in letters[8:12]:
    first_word.append(char)

for char in letters[12:20]:
    second_word.append(char)
second_word.append(" ")

for char in letters[-8:-1:1]:
    third_word.append(char)
third_word.append(",")
third_word.append(" ")

for char in letters[:-23:1]:
    fourth_word.append(char)
fourth_word.append(".")

position_changed = ''.join(first_word) + ''.join(second_word) + ''.join(third_word) + ''.join(fourth_word)

print(''.join(letters))
print(position_changed)