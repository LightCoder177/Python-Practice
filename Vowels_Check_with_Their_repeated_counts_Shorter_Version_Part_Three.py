#Checking for vowels with their repeated counts without repeating the non-repeated vowels.

#list and variable.

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
found = {}


word = input("Please type your sentence here: ")

#loop and execution

for letter in word:
    if letter in vowels:
        if letter in found:
            found[letter] += 1
        else:
            found[letter] = 0
            found[letter] += 1


print("Here are the vowels with their repeated counts in the sentence that you provided.")

for vowel, count in found.items():
    if vowel in word:
        print("{0:s} found {1:d} time(s).".format(vowel, count))
    