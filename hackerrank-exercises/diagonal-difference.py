"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1+5+9 . The right to left diagonal = 3+5+9. Their absolute difference is |15-17| = 2.

Function description

Complete the  function in the editor below.

diagonalDifference takes the following parameter:
int arr[n][m]: an array of integers

Return:
int: the absolute diagonal difference
"""

#https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # lendiagonal_one = 0
    diagonal_two = 0
    for index, items in enumerate(arr):
        diagonal_one += items[index]
    print(diagonal_one)
    for index, items in enumerate(arr):
        items = items[::-1]
        diagonal_two += items[index]
    print(diagonal_two)
    print(abs(diagonal_one - diagonal_two))
    return abs(diagonal_one - diagonal_two)
    
num = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
diagonalDifference(num)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = []

#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = diagonalDifference(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()