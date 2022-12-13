#Vowel check with tuple

#tuple and set

vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
found = set()

#input variable

word = input("Please type your sentence here: ")

#loop, condition, and execution

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.add(letter)

print("We found these common vowels in your setnence: ")

for vowel in sorted(found):
    print(vowel)