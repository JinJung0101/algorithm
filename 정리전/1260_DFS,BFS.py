from collections import deque


def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    q = deque([start]) 
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in graph:
    i.sort()


visited = [False]*(N+1)
dfs(V)
print()

visited = [False]*(N+1)
bfs(V)
