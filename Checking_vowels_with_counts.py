#Checking vowels and their repeated counts. 

#list and dictionary

vowels = ['a', 'A', 'e','E', 'i', 'I', 'o', 'O', 'u', 'U']
found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0
found['A'] = 0
found['E'] = 0
found['I'] = 0
found['O'] = 0
found['U'] = 0

word = input("Type your sentence here: ")

#loop and execution

for letters in word:
    if letters in vowels:
        found[letters] += 1

print("Here are the vowels and their repeated count.")

for vowel, count in found.items():
    print("{0:s} found {1:d} time(s).".format(vowel, count))
