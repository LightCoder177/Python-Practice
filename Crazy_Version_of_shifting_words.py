#shifting words to another list without changing the original and the meaning.

#variable and list.

paranoid_android = "Marvin, The Paranoid Android."
first_word = []
second_word = []
third_word = []
fourth_word = []

letters = list(paranoid_android)

#loop and execution.

for char in letters[8:11]:
    first_word.append(char)

for char in letters[11:20]:
    second_word.append(char)
second_word.append(" ")

for char in letters[-8:-1]:
    third_word.append(char)
third_word.append(letters[6])
third_word.append(letters[7])

for char in letters[:-23:1]:
    fourth_word.append(char)
fourth_word.append(letters[-1])

Changed_Phrased = ''.join(first_word) + ''.join(second_word) + ''.join(third_word) + ''.join(fourth_word)

print(''.join(letters))
print(Changed_Phrased)