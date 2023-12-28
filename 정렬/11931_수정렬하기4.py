import sys

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

nums.sort(reverse=True)

for i in nums:
    print(i)