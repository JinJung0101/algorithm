from collections import deque

def bfs(a, b):
    queue = deque([(a, b)])
   
    while queue:
        x, y = queue.popleft()
        if floor[x][y] == "-":
            floor[x][y] = "1"
            # 바닥 밖으로 나가지않거나 옆으로 이동했을 때 같은 종류라면
            if y+1 < m and floor[x][y+1] == "-":
                queue.append((x, y+1))
        elif floor[x][y] == "|":
            floor[x][y] = "1"
            # 바닥 밖으로 나가지않거나 아래로 이동했을 때 같은 종류라면
            if x+1 < n and floor[x+1][y] == "|":
                queue.append((x+1, y))

#세로 N, 가로 M 
n, m = map(int, input().split())

# 바닥정보를 넣을 리스트
floor = [list(input()) for _ in range(n)]

#나무판자의 개수 
cnt = 0


for i in range(n):
    for j in range(m):
        if floor[i][j] != "1":
            bfs(i, j)
            cnt += 1


print(cnt)