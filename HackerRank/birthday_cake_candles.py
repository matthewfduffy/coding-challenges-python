# HackerRank
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

"""
You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest. 

Sample I/O:
    candles = [4, 4, 1, 3] -> 2

Explanation: 
    The max height candle(s) is 4 and there are two of them.
"""
from collections import Counter

def birthdayCakeCandles(candles):
    # sort the passed-in array so the highest value is the first index
    candles.sort(reverse=True)
    # Create a counter object of the candles array; assign to variable
    candle_count = Counter(candles)
    # Access the value in the counter object where key is set to the highest value in the candles-array
    val = candle_count.get(candles[0])
    print(val)


arr = [4, 4, 1, 3]
birthdayCakeCandles(arr)