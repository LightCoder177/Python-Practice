#Vowel checking function

#function

def vowel_check(word: str) -> set:
    """Return as true or false if found a vowel in the provided phrase."""
    vowels = set("AEIOUaeiou")
    found = vowels.intersection(set(word))
    return bool(found)