# HackerRank Min-Max-Sum
# https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true

"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers. 

Sample Input:   arr = [1, 3, 5, 7, 9]
Sample Output:  16 24
Explanation:
    Minimum Sum is 1+3+5+7=16
    Maximum Sum is 3+5+7+9=24
"""
from functools import reduce

def minMaxSum(arr):
    arr.sort()
    min_arr = reduce(lambda x,y: x + y, arr[:4])
    max_arr = reduce(lambda x,y: x + y, arr[1:5])
    print(min_arr, max_arr)
    


myArr = [1, 3, 5, 7, 9]
minMaxSum(myArr)