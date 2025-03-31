# Returns an integer value passed into the function with it's ordinal suffix (i.e. - 'th', 'st', 'rd)

def ordinal_suffix(value):
    s = str(value)
    if s.endswith('11'):
        return s + 'th'
    elif s.endswith('12'):
        return s + 'th'
    elif s.endswith('13'):
        return s + 'th'
    elif s.endswith('1'):
        return s + 'st'
    elif s.endswith('2'):
        return s + 'nd'
    elif s.endswith('3'):
        return s + 'rd'
    else:
        return s + 'th'


# Test Case(s)
print(ordinal_suffix(15))
print(ordinal_suffix(25))