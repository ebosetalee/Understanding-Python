"""
This is a staircase of size :

   #
  ##
 ###
####
Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.

Function Description:
Complete the staircase function in the editor below.

staircase has the following parameter(s):
int n: an integer

Print:
Print a staircase as described above.

"""
# https://www.hackerrank.com/challenges/staircase/problem?h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    length = 1
    hashs = "#"
    while length <= n:
        space = " "
        print("{0}{1}"
        .format(space* (n-length), hashs *length))
        length +=1

staircase(10)

# if __name__ == '__main__':
#     n = int(input())

#     staircase(n)
