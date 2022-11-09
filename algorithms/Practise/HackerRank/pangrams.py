"""A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

Example
The string contains all letters in the English alphabet, so return pangram.
"""

s = "We promptly judged antique ivory buckles for the prize"


def pangrams(s):
    # Write your code here
    a = len(set(s.lower()))
    if a == 27:
        return "pangram"
    else:
        return "not pangram"


print(pangrams(s))
