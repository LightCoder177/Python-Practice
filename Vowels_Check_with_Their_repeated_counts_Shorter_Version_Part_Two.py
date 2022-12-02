#Checking for vowels and their repeated counts(Frequency count in techincal count)

#list and count

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
found = {}

for letters in vowels:
    found[letters] = 0

word = input("Type your sentence here: ")

#loop and execution

for letters in word:
    if letters in vowels:
        found[letters] += 1
print("Here are the vowels with their repeated counts in the sentences that you provided.")

for vowel, count in found.items():
    if vowel in word:
        print("{0:s} found {1:d} time(s).".format(vowel, count))
    