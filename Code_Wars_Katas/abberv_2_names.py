"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
"""
# Option 1
def abbrev_name(name):
    initials = name.split(" ")
    return str(initials[0][0] + "." + initials[1][0]).upper()





test_name = "mike jones"
print(abbrev_name(name))