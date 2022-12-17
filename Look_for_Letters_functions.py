#Checking for letters in the provided phrase.

#function

def letter_check(phrase: str, letters:str) -> set:
    """Check for requested letters in the provided phrase."""
    return set(letters).intersection(set(phrase))
