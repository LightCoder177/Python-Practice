#A short version of vowel checking program using set. 

#set

vowels = {'a', 'e', 'i',' o', 'u', 'A', 'E', 'I', 'O', 'U'}

word = input("Please type your sentence here: ")

found = vowels.intersection(set(word))

#Execution

print("Here are the vowels in the sentence that you provided.")

for vowel in sorted(found):
    print(vowel)