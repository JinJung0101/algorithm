# 최단거리 구하기 (BFS)

from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
distance = [-1]*(n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

d = [-1]*(n+1) #노드 간 거리 -1초기화
d[x] = 0

q = deque([x])
while q:
    start = q.popleft() #현재노드 pop

    for nx in graph[start]: #현재 갈 수 있는 모든 노드 탐색
        if d[nx] == -1: #방문한적없는 노드라면
            d[nx] = d[start] + 1 #방문처리
            q.append(nx)

check = False

for i in range(1, n+1):
    if d[i]==k:
        print(i)
        check = True

if check == False:
    print(-1)

