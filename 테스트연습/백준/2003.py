from collections import deque

n, m = map(int, input().split())
nums = [*map(int, input().split())]

q = deque()
temp = 0
ans = 0
for i in nums:
    q.append(i)
    temp += i
    if temp >= m:
        if temp == m:
            ans += 1
            continue
        while temp > m:
            t = q.popleft()
            temp -= t
        if temp == m:
            ans += 1
            continue

print(ans)