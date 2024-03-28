import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = dict()
b = []
ans = 0
for _ in range(n):
    d[input().rstrip()] = 1
for _ in range(m):
    t = input().rstrip()
    if t in d:
        b.append(t)
        ans += 1

print(ans)
b.sort()
for i in b:
    print(i)