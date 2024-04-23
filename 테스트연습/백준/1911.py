import sys
input = sys.stdin.readline

n, l = map(int, input().split())
puddle = []
for _ in range(n):
    a, b = map(int ,input().split())
    puddle.append((a, b))

puddle.sort()
ans = 0
last_puddle = 0
for p in puddle:
    if p[1] <= last_puddle:
        continue

    start = max(p[0], last_puddle)
    temp = (p[1] - start) // l
    if (p[1] - start) % l != 0:
        temp += 1
    ans += temp
    last_puddle = start+temp*l

print(ans)