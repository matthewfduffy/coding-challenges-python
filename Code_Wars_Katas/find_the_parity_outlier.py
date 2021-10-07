"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# Examples:
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""
def find_outlier(integers):
    tmp_list = []
    even_num = 0
    odd_num = 0

    for int in integers:
        if int % 2 == 0:
            even_num = int
            tmp_list.append(0)
        else:
            odd_num = int
            tmp_list.append(int)

    tmp_list.sort()
    if tmp_list[-2] == 0:
        return odd_num
    else:
        return even_num