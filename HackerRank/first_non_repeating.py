"""
Write a function named `first_non_repeating_letter` that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("");

† Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character.
"""

def first_non_repeating_letter(s):
    current = 0
    future = 1

    while future < len(s):
        print(f"this is iteration {future}")
        if s[current].lower() == s[future].lower():
            current += 1
            future += 1
        else:
            return s[future]






test_1 = "stress"
test_2 = "sstress"
test_3 = "sTreSS"
test_4 = "sSS"
print(first_non_repeating_letter(test_1))
print(first_non_repeating_letter(test_2))
print(first_non_repeating_letter(test_3))
print(first_non_repeating_letter(test_4))