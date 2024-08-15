from sys import stdin, setrecursionlimit
from collections import deque

setrecursionlimit(10000)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start):
    queue = deque([start])
    visited = [False] * (len(graph) + 1)
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
print("DFS:")
dfs(graph, v, visited)
print("\nBFS:")
bfs(graph, v)
