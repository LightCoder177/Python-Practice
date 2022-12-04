#Creating a shoter version of checking the vowel program. 

#set. 

vowels = {'a', 'e', 'i', 'o', 'u'}

word = input("Please type your sentence here: ")

#execution

found = vowels.intersection(set(word))

print("Here are the vowels found in your sentence.")

for vowel in sorted(found):
    print(vowel)