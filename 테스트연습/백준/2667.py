def dfs(x, y):
    # 이동할 네 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 스택을 사용한 DFS
    stack = [(x, y)]
    count = 0
    
    while stack:
        cx, cy = stack.pop()
        
        if visited[cx][cy]:
            continue
        
        visited[cx][cy] = True
        count += 1
        
        # 네 방향으로 이동
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 1:
                stack.append((nx, ny))
    
    return count

# 입력 받기
N = int(input())
grid = [list(map(int, input().strip())) for _ in range(N)]

# 방문 배열 초기화
visited = [[False] * N for _ in range(N)]
complexes = []

# 모든 칸을 순회하며 DFS로 단지 찾기
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:
            complex_size = dfs(i, j)
            complexes.append(complex_size)

# 단지 크기를 오름차순으로 정렬
complexes.sort()

# 결과 출력
print(len(complexes))
for size in complexes:
    print(size)
