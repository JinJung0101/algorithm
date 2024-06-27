from collections import deque

def bfs(start, graph, n):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 0

    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    graph = [[] for _ in range(n + 1)]
    
    index = 2
    for _ in range(m):
        a = int(data[index])
        b = int(data[index + 1])
        graph[b].append(a)
        index += 2
    
    max_count = 0
    result = []
    
    for i in range(1, n + 1):
        count = bfs(i, graph, n)
        if count > max_count:
            max_count = count
            result = [i]
        elif count == max_count:
            result.append(i)
    
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
