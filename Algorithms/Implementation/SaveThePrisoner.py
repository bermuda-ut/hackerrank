#!/bin/python3

# https://www.hackerrank.com/challenges/save-the-prisoner

t = int(input())

for x in range(t):
    n, m, s = [int(x) for x in input().strip().split()]
    z = -1 + (s + m) % n

    if(z == 0):
        print(n)
    else:
        print(z)
