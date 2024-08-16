from sys import stdin
from collections import deque

def bfs(grid, start, n, m):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([start])
    distances = [[-1] * m for _ in range(n)]
    distances[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        current_distance = distances[x][y]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and distances[nx][ny] == -1:
                distances[nx][ny] = current_distance + 1
                queue.append((nx, ny))

    # Output the distances
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                print(-1, end=' ')
            else:
                print(distances[i][j], end=' ')
        print()

def main():
    input = stdin.read
    data = input().split()
    n, m = int(data[0]), int(data[1])
    grid = []
    start = None

    index = 2
    for i in range(n):
        row = []
        for j in range(m):
            cell = int(data[index])
            index += 1
            row.append(cell)
            if cell == 2:
                start = (i, j)
        grid.append(row)

    if start:
        bfs(grid, start, n, m)

if __name__ == "__main__":
    main()
