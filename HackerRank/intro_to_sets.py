# HackerRank > Practice > Python > Sets > Intro to Sets
"""
    [TASK]
    Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse. 
    Average = Sum of Distinct Heights / Total Number of Distinct Heights

    Complete the average function 

    [Input]:    int arr: an array of integers
    The first line contains the integer N (the size of arr)
    The second line contains the N space separated integers, arr[i]
    
    [Returns]:  float: the resulting float value rounded to 3 places after the decimal

    [Sample Input]:
    10              arr[] size N = 10
    [161, 182, 161, 154, 178, 170, 167, 171, 170, 174]      arr = [161, 181,...,174]

    [Sample Output]:
    169.375
"""
def average(array):     # base
    arr_length = len(array)
    unique_array = set(array)
    avg = sum(unique_array) / len(unique_array)
    print(avg)

average([161, 182, 161, 154, 178, 170, 167, 171, 170, 174])

#submitted
