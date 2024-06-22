import sys
sys.setrecursionlimit(10000)

def dfs(x, y, height):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and area[nx][ny] > height:
                visited[nx][ny] = True
                stack.append((nx, ny))

# 입력 받기
N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

# 지역의 최대 높이 확인
max_height = max(max(row) for row in area)

# 결과 변수 초기화
max_safe_areas = 0

# 모든 높이에 대해 안전 영역 개수 계산
for h in range(max_height + 1):
    visited = [[False] * N for _ in range(N)]
    safe_areas = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] > h and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j, h)
                safe_areas += 1
    max_safe_areas = max(max_safe_areas, safe_areas)

# 결과 출력
print(max_safe_areas)
