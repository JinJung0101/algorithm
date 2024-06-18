from collections import deque

def bfs(start, end):
    queue = deque([(start, 0)])  # (현재 사람, 촌수)
    visited = [False] * (N + 1)
    visited[start] = True
    
    while queue:
        current, count = queue.popleft()
        
        if current == end:
            return count
        
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, count + 1))
    
    return -1

# 입력 받기
N = int(input())
A, B = map(int, input().split())
M = int(input())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

# 관계 입력 받기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# BFS를 사용하여 촌수 계산
result = bfs(A, B)
print(result)
