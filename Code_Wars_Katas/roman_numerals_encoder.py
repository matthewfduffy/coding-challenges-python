"""
    Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

    Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

    [Example]:
    solution(1000)  # should return 'M'

    [Mapping]:
    I       1
    V       5
    X       10
    L       50
    C       100
    D       500
    M       1000

    Remember that there can't be more than 3 identical symbols in a row.

    More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals
"""

def solution(n):
    n_string = str(n)
    n_length = len(n_string)
    roman_string = ''

    if n_length == 4:
        roman_string += "M" * int(n_string[0])
        n_string = n_string[1:]
        n_length -= 1

    if n_length == 3:
        x = int(n_string[0])
        if x == 9:
            roman_string += "CM"
        elif x >= 5:
            roman_string += "D"
            roman_string += "C" * (x - 5)
        elif x == 4:
            roman_string += "CD"
        else:
            roman_string += "C" * x

        n_string = n_string[1:]
        n_length -= 1

    if n_length == 2:
        x = int(n_string[0])
        if x == 9:
            roman_string += "XC"
        elif x >= 5:
            roman_string += "L"
            roman_string += "X" * (x - 5)
        elif x == 4:
            roman_string += "XL"
        else:
            roman_string += "X" * x

        n_string = n_string[1:]
        n_length -= 1

    if n_length == 1:
        x = int(n_string[0])
        if x == 9:
            roman_string += "IX"
        elif x >= 5:
            roman_string += "V"
            roman_string += "I" * (x - 5)
        elif x == 4:
            roman_string += "IV"
        else:
            roman_string += "I" * x


    return roman_string