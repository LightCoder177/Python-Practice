#Checking for vowels and their repeated counts(frequence counts in technical terms)

#list and dict. 

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
found = {}

for letters in vowels:
    found[letters] = 0

word = input("Type your sentence here: ")

#loop and execution

for letters in word:
    if letters in vowels:
        found[letters] += 1

print("Here are the vowels and their repeated counts")

for vowel, count in found.items():
    print("{0:s} found {1:d} time(s).".format(vowel, count))
