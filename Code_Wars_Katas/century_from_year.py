"""
The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

[Task]
Given a year, return the century it is in.

[Examples]

1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
2742 --> 28
"""
def century(year):
    year_to_string = str(year)
    if len(year_to_string) < 4:
        if len(year_to_string) == 3:
            if year_to_string[-2:] == "00":
                return int(year_to_string[:1])
            else:
                return int(year_to_string[:1]) + 1
        else:
            return 1
    else:
        if year_to_string[-2:] == "00":
            return int(year_to_string[:2])
        else:
            return int(year_to_string[:2]) + 1


# Alternate Options
# Option 1
def century(year):
    return (year + 99) // 100

# Option 2
import math

def century(year):
    return math.ceil(year / 100)

# Option 3
def century(year):
    if year%100==0:
        return year//100
    else:
        return year//100+1

# Option 4
def century(year):
    return (year / 100) if year % 100 == 0 else year // 100 + 1

# Option 5
def century(year):
    return (year - 1) // 100 + 1


# Test
test_a = 1705
test_b = 1900
test_c = 1601
test_d = 2000
test_e = 2742
test_f = 356
test_g = 90
test_h = 2240
test_i = 400
test_j = 207

print(century(test_a))
print(century(test_b))
print(century(test_c))
print(century(test_d))
print(century(test_e))
print(century(test_f))
print(century(test_g))
print(century(test_h))
print(century(test_i))
print(century(test_j))