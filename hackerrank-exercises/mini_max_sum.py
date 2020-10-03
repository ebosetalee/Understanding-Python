"""
Given five positive integers, find the minimum and maximum values that can be 
calculated by summing exactly four of the five integers. Then print the respective 
minimum and maximum values as a single line of two space-separated long integers.

Example:
arr = [1,3,5,7,9]
The minimum sum is 1 + 3 + 5 + 7 = 16 and the maximum sum is 3 + 5 + 7 + 9 = 24. 
The function prints:
16 24

Function Description:
Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):
arr: an array of 5 integers

Print:
Print two space-separated integers on one line: 
the minimum sum and the maximum sum of 4 of 5 elements.

Explanation:
The numbers are 1, 2, 3, 4, and 5. 
Calculate the following sums using four of the five integers:
Sum everything except 1, the sum is 2 + 3 + 4 + 5 = 14.
Sum everything except 2, the sum is 1 + 3 + 4 + 5 = 13.
Sum everything except 3, the sum is 1 + 2 + 4 + 5 = 12.
Sum everything except 4, the sum is 1 + 2 + 3 + 5 = 11.
Sum everything except 5, the sum is 1 + 2 + 3 + 4 = 10.
"""
#https://www.hackerrank.com/challenges/mini-max-sum/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max_sum = 0
    min_sum = 0
    loops = 0
    while loops < 5:
        calculated_sum = 0
        for index, items in enumerate(arr):       
            if index != loops:
                calculated_sum += items
        if calculated_sum > max_sum:
            max_sum = calculated_sum
            if loops == 0:
                min_sum = calculated_sum
        elif calculated_sum < min_sum:
            min_sum = calculated_sum
        loops += 1
    print(min_sum, max_sum)
       

miniMaxSum([1,3,5,7,9])
    
# if __name__ == '__main__':
#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)
