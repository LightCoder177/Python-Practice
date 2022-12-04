#A shorter version of vowel checking program. 

#set

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

word = input("Please type your sentence here: ")

#Execution

found = vowels.intersection(set(word))

print("Here are the vowels in your sentence.")

for vowel in sorted(found):
    print(vowel)