import sys

A = set(sys.stdin.readline().split())
B = set(sys.stdin.readline().split())

print(A - B)