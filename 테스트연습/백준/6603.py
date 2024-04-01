import sys
from itertools import combinations
input = sys.stdin.readline

while 1:
    nums = [*map(int, input().split())]
    if len(nums) == 1:
        break
    k = nums.pop(0)
    comb = list(combinations(nums, 6))
    for c in comb:
        print(' '.join(map(str, c)))
    print()