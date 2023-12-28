from collections import deque
import sys

#상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# r,c 숲의 세로가로
r, c = map(int, sys.stdin.readline().split())
# 숲 2차원리스트 생성
forest = [list(sys.stdin.readline())for _ in range(r)]
# 물과 고슴도치가 해당 위치까지 도달하기 위한 최소 시간을 저장할 2차원 리스트, 초기값 -1: 아직방문 x
water = [[-1]*c for _ in range(r)]
hedgehog = [[-1]*c for _ in range(r)]

water_q = deque()
hedgehog_q = deque()


def bfs():
    #물이 차오르는 부분 처리
    while water_q:
        x, y = water_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

               #범위를 벗어나거나 돌('X') 또는 비버의 굴('D')인 경우 스킵
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if forest[nx][ny] != 'D' and forest[nx][ny] != 'X' and water[nx][ny] == -1:
                water[nx][ny] = water[x][y] + 1
                water_q.append((nx,ny))
    
    #고슴도치가 움직이는 부분 처리
    while hedgehog_q:
        x, y = hedgehog_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #범위를 벗어나거나 돌('X') 또는 비버의 굴('D')인 경우 스킵
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if forest[nx][ny] == 'D':
                print(hedgehog[x][y] + 1)
                return
            if forest[nx][ny] != 'X' and hedgehog[nx][ny] != '-1' and (water[nx][ny]==-1 or hedgehog[x][y]+1<water[nx][ny]):
                hedgehog[nx][ny] = hedgehog[x][y] + 1
                hedgehog_q.append((nx,ny))
    print("KAKTUS")

for i in range(r):
    for j in range(c):
        if forest[i][j]=='*':
            water[i][j]=0
            water_q.append((i,j))
        elif forest[i][j] == 'S':
            hedgehog_q.append((i,j))
            hedgehog[i][j]=0

bfs()

