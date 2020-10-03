"""
Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. 
Given an array of integers representing the color of each sock, determine how many pairs of socks with 
matching colors there are.

For example, there are n = 7 socks with colors ar = [1,2,1,2,1,3,2]. 
There is one pair of color 1 and one of color 2. There are three odd socks left, 
one of each color. The number of pairs is 2.

Function Description:
Complete the sockMerchant function in the editor below. 
It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):
n: the number of socks in the pile
ar: the colors of each sock

Input Format:
The first line contains an integer n, the number of socks represented in ar.
The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile.

Constraints:
1 <= n <= 100
1 <= ar[i] <= 100 where 0 <= i < n

Output Format:
Return the total number of matching pairs of socks that Alex can sell.
"""
# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pair = 0
    sock_dict = {}
    for color in ar:
        if color in sock_dict:
            sock_dict[color] += 1
        else:
            sock_dict[color] = 1 
    print(sock_dict)      
    for item in sock_dict:
        pair += int(sock_dict[item] /2)
    print(pair)
    return pair
        
sockMerchant(7, [10,20,20,10,10,30,50,10,20])
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()
