import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()
i, j = 0, 1
ans = 2e9
while j < n:
    diff = nums[j] - nums[i]
    if i < j and diff >= m:
        if diff < ans:
            ans = diff
        i += 1
    else:
        j += 1

print(ans)