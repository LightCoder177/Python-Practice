#check for letters in phrase with vowels as a default value.

#function

def check_letters(phrase:str, letters:str="aeiouAEIOU") -> set:
    """return a set of letters requested to found in phrase."""
    return set(letters).intersection(set(phrase))
