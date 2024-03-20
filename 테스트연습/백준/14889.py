import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append([*map(int, input().split())])
ans = 1e9


def answer(arr):
    global ans
    a, b = 0, 0
    t2 = []
    for j in range(n):
        if j not in arr:
            t2.append(j)
    for t in arr:
        for tt in arr:
            a += graph[t][tt]
    for s in t2:
        for ss in t2:
            b += graph[s][ss]
    if abs(a - b) < ans:
        ans = abs(a - b)


def dfs(i, t1, c):
    t1.append(i)
    c += 1
    if c == n//2:
        answer(t1)
    else:
        for k in range(i+1, n):
            dfs(k, t1, c)
    t1.remove(i)


for p in range(n//2):
    dfs(p, [], 0)
print(ans)