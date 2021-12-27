"""
    A square of squares

    You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

    However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.
    
    [Task]

    Given an integral number, determine if it's a square number:

    In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

    The tests will always use some integral number, so don't worry about that in dynamic typed languages.

    [Examples]:
    -1  --> False
    0   --> True
    3   --> False
    4   --> True
    25  --> True
    26  --> False
"""
import math

def is_square(n):
    if n < 0:
        return False
    else:
        x = str(math.sqrt(n))
        y = x.split('.')
        if y[1] == str(0):
            return True
        else: 
            return False


print(is_square(25))
print(is_square(26))
print(is_square(-1))
