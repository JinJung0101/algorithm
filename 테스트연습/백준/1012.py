import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    # 이동할 네 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 현재 위치 방문 표시
    visited[x][y] = True
    
    # 네 방향으로 이동
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and field[nx][ny] == 1:
            dfs(nx, ny)

# 입력 받기
T = int(input())
results = []

for _ in range(T):
    M, N, K = map(int, input().split())
    
    # 밭 초기화
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    # 배추 위치 입력 받기
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    # 구역 수 계산
    count = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1
    
    results.append(count)

# 결과 출력
for result in results:
    print(result)
