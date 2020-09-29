"""
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, 
awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), 
and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

If a[i] > b[i], then Alice is awarded 1 point.
If a[i] < b[i], then Bob is awarded 1 point.
If a[i] = b[i], then neither person receives a point.
Comparison points is the total points a person earned.

Given a and b, determine their respective comparison points.
"""
# https://www.hackerrank.com/challenges/compare-the-triplets/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplet(a, b):
    compared_points = []
    loop = 0
    for items in a:
        if a[loop] > b[loop]:
            compared_points.append(1)
        elif a[loop] < b[loop]:
            compared_points.append(1)
        else:
            pass
        loop += 1
    print(compared_points)
    return compared_points

compareTriplet([1,2,3], [3,2,1])

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     a = list(map(int, input().rstrip().split()))

#     b = list(map(int, input().rstrip().split()))

#     result = compareTriplets(a, b)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()

# def compareTriplets(a, b):
#     a_point = 0
#     b_point = 0
#     loop = 0
#     for items in a:
#         if a[loop] > b[loop]:
#             a_point += 1
#         elif a[loop] < b[loop]:
#             b_point += 1
#         else:
#             pass
#         loop += 1
#     print(a_point, b_point)
#     return a_point, b_point

# compareTriplets([17,28,30],[99,16,8])

# Another solution:
def compareTriplets(a, b):
    a_point = 0
    b_point = 0
    # loop = 0
    for index, items in enumerate(a):
        if a[index] > b[index]:
            a_point += 1
        elif a[index] < b[index]:
            b_point += 1
        else:
            pass
        # print(index)
        # loop += 1
    print(a_point, b_point)
    return a_point, b_point

compareTriplets([17,28,30],[99,16,8])

