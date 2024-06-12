from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    building = []
    for _ in range(h):
        building.append([*map(str, input().rstrip())])

    q = deque()
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                q.append((i, j, 0, '*'))
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                q.append((i, j, 0, '@'))

    can_escape = False
    while q:
        x, y, c, S = q.popleft()

        if x == 0 or x == h-1 or y == 0 or y == w-1:
            if S == '@':
                can_escape = True
                print(c+1)
                break

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and building[nx][ny] == '.':
                building[nx][ny] = S
                q.append((nx, ny, c+1, S))

    if not can_escape:
        print("IMPOSSIBLE")