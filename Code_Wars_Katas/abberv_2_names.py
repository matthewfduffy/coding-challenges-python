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

# Option 2
def abbrev_name2(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]

# Option 3
def abbrev_name3(name):
    return '.'.join(w[0] for w in name.split()).upper()


# Option 4
def abbrev_name4(name):
    initials = name.split()
    return f"{initials[0][0]}.{initials[1][0]}".upper()

test_name = "mike jones"
print(abbrev_name(name))