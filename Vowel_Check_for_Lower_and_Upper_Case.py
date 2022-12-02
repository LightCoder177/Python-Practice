#Creating a program that will check for vowels in a sentence. 

#List and variable

vowels_lowercase = ['a', 'e', 'i', 'o', 'u']
vowels_uppercase = ['A', 'E', 'I', 'O', 'U']
found = []
word = input("Please provide us with a sentence: ")

#loop and execution.

for letter in word:
    if letter in vowels_lowercase or letter in vowels_uppercase:
        if letter not in found:
            found.append(letter)

print()
print("Here are the vowels in the sentence that you provided: ")
for vowel in found:
    print(vowel)