#!/bin/python3

# https://www.hackerrank.com/challenges/tutorial-intro

v = int(input())
n = int(input())
array = [int(x) for x in input().strip().split()]

print(array.index(v))
