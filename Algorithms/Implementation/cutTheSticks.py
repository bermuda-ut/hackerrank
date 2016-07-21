#!/bin/python3

# https://www.hackerrank.com/challenges/cut-the-sticks

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

while arr:
	print(len(arr))
	currMin = min(arr)
	arr = [x - currMin for x in arr if x != currMin]