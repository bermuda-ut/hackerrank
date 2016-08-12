#!/bin/python3

# https://www.hackerrank.com/challenges/fibonacci-modified

t1, t2, n = [int(x) for x in input().strip().split()]

t = [-1] * n
t[0], t[1] = t1, t2

for i in range(2, n):
	t[i] = t[i-2] + t[i-1] ** 2

print(t[n-1])