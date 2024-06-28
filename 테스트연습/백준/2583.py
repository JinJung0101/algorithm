from collections import deque

def bfs(x, y, paper, visited, M, N):
    queue = deque([(x, y)])
    visited[x][y] = True
    area = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        cx, cy = queue.popleft()
        area += 1
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and not paper[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    return area

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    M = int(data[0])
    N = int(data[1])
    K = int(data[2])
    
    paper = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    
    index = 3
    for _ in range(K):
        x1 = int(data[index])
        y1 = int(data[index + 1])
        x2 = int(data[index + 2])
        y2 = int(data[index + 3])
        for i in range(y1, y2):
            for j in range(x1, x2):
                paper[i][j] = 1
        index += 4
    
    areas = []
    
    for i in range(M):
        for j in range(N):
            if not visited[i][j] and not paper[i][j]:
                area = bfs(i, j, paper, visited, M, N)
                areas.append(area)
    
    areas.sort()
    
    print(len(areas))
    print(" ".join(map(str, areas)))

if __name__ == "__main__":
    main()
