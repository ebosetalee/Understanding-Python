"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example:
s = "12:01:00PM
Return "12:01:00".

s = "12:01:00PM"
Return "00:01:00".

Function Description:
Complete the timeConversion function in the editor below. 
It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):
string s: a time in 12 hour format

Returns:
string: the time in 24 hour format
"""
# https://www.hackerrank.com/challenges/time-conversion/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:] == "PM":
        if s[:2] == "12":
            print(s[0:8])
        else:
            added_time = int(s[:2]) + 12
            print(str(added_time) + s[2:8])
    else:
        if s[:2] == "12":
            print("00"+ s[2:8])
        else:
            print(s[:8]) 


timeConversion("2:05:45 AM")

# if __name__ == '__main__':
#     f = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = timeConversion(s)

#     f.write(result + '\n')

#     f.close()
