from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append([*map(int, input().split())])


def distinguish_island(x_cor, y_cor, index, array):
    global n
    q = deque([(x_cor, y_cor)])
    visited[x_cor][y_cor] = 1
    array[x_cor][y_cor] = index
    while q:
        x, y = q.popleft()
        for t in range(4):
            nx, ny = x + dt[t][0], y + dt[t][1]
            if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                array[nx][ny] = index
                q.append((nx, ny))


def shortest_bridge(x_cor, y_cor, index, array):
    global n
    is_visit = [[0 for _ in range(n)] for _ in range(n)]
    q = deque([(x_cor, y_cor, 0)])
    is_visit[x_cor][y_cor] = 1
    while q:
        x, y, l = q.popleft()
        for t in range(4):
            nx, ny = x + dt[t][0], y + dt[t][1]
            if 0 <= nx < n and 0 <= ny < n and not is_visit[nx][ny]:
                if array[nx][ny] == 0:
                    q.append((nx, ny, l+1))
                    is_visit[nx][ny] = 1
                elif array[nx][ny] != index:
                    return l


# 섬 구분 짓기
idx = 1
dt = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            distinguish_island(i, j, idx, arr)
            idx += 1

# 다리 놓기
ans = 10000
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            length = shortest_bridge(i, j, arr[i][j], arr)
            if length is not None and length < ans:
                ans = length

print(ans)