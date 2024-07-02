from collections import deque

def bfs(maze, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '1':
                maze[nx][ny] = maze[x][y] + 1  # 거리를 기록하며 방문 처리
                queue.append((nx, ny))
    return maze[n-1][m-1]

# 입력
n, m = map(int, input().split())
maze = [list(input().strip()) for _ in range(n)]
maze[0][0] = 1  # 시작점 초기화

# BFS 실행 및 결과 출력
print(bfs(maze, n, m))
