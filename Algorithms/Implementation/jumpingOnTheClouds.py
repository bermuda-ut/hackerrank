#!/bin/python3

# Solution for https://www.hackerrank.com/challenges/jumping-on-the-clouds

import sys

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

mustVisit = [i for i in range(0,n-1) if c[i+1] == 1 and c[i] == 0]

currPos = 0
jump = 0

while currPos < n-1:
	if(mustVisit):
		toVisit = mustVisit.pop(0)
	else:
		toVisit = 0

	while(toVisit and currPos < toVisit):
		if(currPos+1 == toVisit):
			currPos += 1
		else:
			currPos += 2
		jump += 1

	currPos += 2
	jump += 1

print(jump)
