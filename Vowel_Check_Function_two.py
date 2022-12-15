#Creating a vowel check function

#Function

def Vowel_Check(word:str) -> set:
    """Check for vowels in a requested phrase and display them"""
    vowels = set("aeiouAEIOU")
    return vowels.intersection(set(word))

