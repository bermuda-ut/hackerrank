#!/bin/python3

# Solution for https://www.hackerrank.com/challenges/equal-stacks

import sys

n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]


all = [h1, h2, h3]
heights = [sum(h1), sum(h2), sum(h3)] # pre-calculated heights
i 		= [0, 0, 0] # starting index for the all stack

# greed is good,
# cut off the heighest stack
maxH = max(heights)
maxi = heights.index(maxH)

while(not (heights[0] == heights[1] and heights[1] == heights[2])):
	heights[maxi] = heights[maxi] - all[maxi][i[maxi]]
	i[maxi] += 1
	maxH = max(heights)
	maxi = heights.index(maxH)

print(heights[0])