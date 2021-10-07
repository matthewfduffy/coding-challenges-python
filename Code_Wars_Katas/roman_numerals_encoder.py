"""

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