from collections import deque

def bfs(n, k):
    if n >= k:
        return n - k
    
    deque_ = deque([n])
    visited = [float('inf')] * 100001
    visited[n] = 0

    while deque_:
        current = deque_.popleft()
        time = visited[current]
        
        if current * 2 <= 100000 and visited[current * 2] > time:
            visited[current * 2] = time
            deque_.appendleft(current * 2)
        if current + 1 <= 100000 and visited[current + 1] > time + 1:
            visited[current + 1] = time + 1
            deque_.append(current + 1)
        if current - 1 >= 0 and visited[current - 1] > time + 1:
            visited[current - 1] = time + 1
            deque_.append(current - 1)

    return visited[k]

n, k = map(int, input().split())

print(bfs(n, k))
