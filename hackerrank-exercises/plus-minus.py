"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
though answers with absolute error of up to  are acceptable.

Example:
arr = [1, 1, 0, -1, -1]
There are  elements, two positive, two negative and one zero. Their ratios are 2/5 = 0.40000, 2/5 = 0.40000 and 1/5 = 0.200000 . Results are printed as:
0.400000
0.400000
0.200000

Function Description:
Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):
int arr[n]: an array of integers
Print:
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with 
6 digits after the decimal. The function should not return a value.
"""
#https://www.hackerrank.com/challenges/plus-minus/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):    
    LENGTH = len(arr)
    positive = 0
    negative = 0
    zeros = 0
    for item in arr:
        if item > 0:
            positive += 1
        elif item == 0:
            zeros += 1
        else:
            negative += 1
    print("{0:.6f}\n{1:.6f}\n{2:.6f}"
    .format(positive / LENGTH, negative /LENGTH, zeros / LENGTH))

plusMinus([1, 1, 0, -1, -1])   

# if __name__ == '__main__':
#     n = int(input())

#     arr = list(map(int, input().rstrip().split()))

#     plusMinus(arr)