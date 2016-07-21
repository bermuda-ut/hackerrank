#!/bin/python3

# https://www.hackerrank.com/challenges/non-divisible-subset

from collections import defaultdict

n, k = [int(x) for x in input().strip().split()]
arr = [int(x) for x in input().strip().split()]

existence = defaultdict(int)

for item in arr:
	existence[item % k] += 1

c = bool(existence[0]) # can always put one of self

i = 1
while i * 2 < k:
	# eg. k=3, either 1 or 2 can go in, choose maximum count
	c += max([existence[i], existence[k-i]])
	i += 1

if(k % 2 == 0):
	# if even number, you can put one of the numbers once
	c += 1

"""
This calculates number of all the possible combinations

c = 0
for i in range(0, k):
	if(i != 0 and i * 2 < k):
		c += existence[i] * (existence[i] - 1) / 2

	for j in range(i + 1, k):
		if((i + j) % k != 0):
			c += existence[i] * existence[j]
"""

print(int(c))