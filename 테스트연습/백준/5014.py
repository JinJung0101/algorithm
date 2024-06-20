from collections import deque

def bfs(start, goal, up, down, max_floor):
    queue = deque([(start, 0)]) # (현재 층, 클릭 수)
    visited = [False] * (max_floor + 1)
    visited[start] = True

    while queue:
        current, clicks = queue.popleft()

        if current == goal:
            return clicks
        
        # 위로 이동
        if current + up <= max_floor and not visited[current + up]:
            visited[current + up] = True
            queue.append((current + up, clicks + 1))

        # 아래로 이동
        if current - down >= 1 and not visited[current - down]:
            visited[current - down] =True
            queue.append((current - down, clicks + 1))

    return "use the stairs"

# 입력
F, S, G, U, D = map(int, input().split())

result = bfs(S, G, U, D, F)
print(result)