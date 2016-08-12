#!/bin/python3

# https://www.hackerrank.com/challenges/bigger-is-greater?h_r=next-challenge&h_v=zen

t = int(input())

def findMin(std, s):
	currMin = -1
	for i in range(len(s)):
		if s[i] > std and (currMin == -1 or s[i] < s[currMin]):
			currMin = i;
	return currMin;

for i in range(0, t):
	w = list(input().strip())
	w = w[::-1]

	p = 0
	for i in range(1,len(w)):
		currMin = findMin(w[i], w[:i])
		if(currMin != -1):
			p = 1
			t = w[currMin]
			w[currMin] = w[i]
			w[i] = t
			w = sorted(w[:i], reverse=True) + w[i:]
			print(''.join(w[::-1]))
			break;

	if not p:
		print("no answer")

