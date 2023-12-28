#최단거리탐색을 위해 bfs사용
#  bfs를 이용해 동, 서, 남, 북을 검사하여 이동했을 때 1인 값을 찾는다. 
#  만약 1이라면 그 전 값에 +1을 하여 이동할 때 지나야 하는 최소 칸 수를 더해준다.
#  마지막 graph[n - 1][m - 1]에는 최소 칸 수의 최종값
import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
graph = []

for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    #  큐를 생성하고 시작 위치를 큐에 추가합니다.
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 칸이 미로의 벽에 닿는지
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
            
    # queue 가 빈상태일 경우 최종 목적지까지 도달한 것
    # N-1, M-1 을 하는 이유는 행, 열은 0부터 시작하기때문
    return graph[N-1][M-1]


print(bfs(0,0))