#Creating a function

#Vowel check function

def Vowel_Check(word):
    """Check for vowels in a provided requested sentence."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    print('Here are the vowels in your sentence:')
    for vowel in sorted(found):
        print(vowel)