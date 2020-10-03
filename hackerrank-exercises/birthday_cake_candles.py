"""
You are in charge of the cake for a child's birthday. 
You have decided the cake will have one candle for each year of their total age. 
They will only be able to blow out the tallest of the candles. 
Count how many candles are tallest.

Example
candles = [4,4,1,3]

The maximum height candles are 4 units high. There are 2 of them, so return 2.

Function Description:
Complete the function birthdayCakeCandles in the editor below.

birthdayCakeCandles has the following parameter(s):
int candles[n]: the candle heights

Returns:
int: the number of candles that are tallest
"""

#https://www.hackerrank.com/challenges/birthday-cake-candles/problem?h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max_cake_height = 0
    tallest_candles = 0
    for items in candles:
        if items > max_cake_height:
            max_cake_height = items
            if tallest_candles == 0:
                tallest_candles += 1
        elif items == max_cake_height:
            tallest_candles += 1
    print(tallest_candles)
    return tallest_candles
        
            
birthdayCakeCandles([44, 53, 31, 27, 77, 60, 66, 77, 26, 36])

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     candles_count = int(input().strip())

#     candles = list(map(int, input().rstrip().split()))

#     result = birthdayCakeCandles(candles)

#     fptr.write(str(result) + '\n')

#     fptr.close()
