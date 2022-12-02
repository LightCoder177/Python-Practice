#This program will check vowel in a sentence or word and will print the vowel on the screen. 

#Creating and storing data

vowels = ['a', 'e', 'i', 'o', 'u']

found_vowels = []

#input section

Words_Or_Sentence = input("Enter your answer here: ")


#Execution section

for letters in Words_Or_Sentence:
    if letters in vowels: 
        if letters not in found_vowels:
            found_vowels.append(letters)
for vowel in found_vowels:
    print(vowel)