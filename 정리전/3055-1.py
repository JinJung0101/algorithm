from collections import deque

# 숲의 크기 입력 받기
r, c = map(int, input().split())

# 숲의 상태를 2차원 리스트로 입력 받기
graph = [list(input()) for _ in range(r)]

# 각 위치를 방문한 시간을 저장하는 2차원 리스트 초기화 (-1은 아직 방문하지 않음을 의미)
visited = [[-1] * c for _ in range(r)]

# 상하좌우 네 방향으로 움직일 때 사용되는 좌표 변화량
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

def bfs():
    q = deque()

    # 물과 고슴도치의 초기 위치 찾아서 큐에 추가하기
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "*":
                q.appendleft((i,j)) # 물은 앞쪽에 추가해서 먼저 처리되게 함
                visited[i][j] = 0   # 시작 위치이므로 시간은 0으로 설정 
            elif graph[i][j] == "S":
                q.append((i,j))     # 고슴도치는 뒤쪽에 추가해서 나중에 처리되게 함 
                visited[i][j] = 0   # 시작 위치이므로 시간은 0으로 설정 

    while q:
        x,y = q.popleft()          # 현재 위치

        for i in range(4):         # 상하좌우 네 방향에 대해 탐색 시작 
            nx, ny= x + dx[i], y + dy[i]

            if not(0 <= nx < r) or not(0 <= ny < c):   continue     # 범위 밖인 경우 스킵  
            if visited[nx][ny] != -1:                  continue     # 이미 방문한 경우 스킵  
            if graph[nx][ny] == "*" or graph[nx][ny]=="X": continue # 다음 위치가 돌('X')이거나 물('*')인 경우 스킵
            
            if graph[nx][ny]=="D" and graph[x][y]=="*": continue    # 다음 위치가 비버의 굴('D')인데 현재가 물('*')인 경우 스킵 
            
            if graph[nx][ny]=="D" and graph[x][y]=="S":             # 다음 위치가 비버의 굴('D')인데 현재가 고슴도치('S')인 경우
                return visited[x][y] + 1                             # 고슴도치가 비버의 굴에 도착한 경우, 현재까지 걸린 시간+1을 반환

            q.append((nx,ny))                                        # 다음 위치를 큐에 추가 
            visited[nx][ny] = visited[x][y] + 1                      # 다음 위치 방문 시간 업데이트
            graph[nx][ny] = graph[x][y]                              # 다음 위치의 상태를 현재 상태로 변경 

    return "KAKTUS"   # 모든 가능한 움직임을 탐색한 후에도 비버의 굴에 도달하지 못했을 때 'KAKTUS' 반환 

print(bfs())         # bfs 함수 실행 결과 출력 
