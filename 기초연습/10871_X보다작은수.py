import sys

a, x = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
for i in range(a):
    if nums[i] < x:
        print(nums[i], end=" ")

