# Vowel checking function.

# function.

def vowel_check(phrase: str) -> str:
    """Return a list of vowels found in user phrase."""
    vowels = set("aeiouAEIOU")
    found = vowels.intersection(set(phrase))

    def repeat(Input: set) -> str:
        """loop the content in the set"""
        for vowel in sorted(Input):
            print(vowel)
    return repeat(found)
