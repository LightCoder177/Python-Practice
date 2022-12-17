#vowel check with boolean. 

#function

def vowel_check(word: str) -> bool:
    """display value as true or false if found a vowel in a given sentence."""
    vowels = set('aeiouAEIOU')
    found = vowels.intersection(set(word))
    return bool(found)
