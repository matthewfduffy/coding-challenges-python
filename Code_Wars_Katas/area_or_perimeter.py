"""
You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
If it is a square, return its area. If it is a rectangle, return its perimeter.

[Sample I/O]
6, 10 --> 32
3, 3 --> 9
"""
def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return l + l + w + w

# Option 2
def area_or_perimeter(l , w):
    return l * w if l == w else (l + w) * 2


# Test
test_a1 = 6
test_a2 = 10
test_b1 = 3
test_b2 = 3

print(area_or_perimeter(test_a1, test_a2))
print(area_or_perimeter(test_b1, test_b2))