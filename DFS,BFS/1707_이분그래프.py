from collections import deque
import sys

def bfs(start):
    queue = deque([start]) #시작점을 큐에 넣음
    color[start] = 1  # 시작점의 색깔(집합)을 1로 설정
    while queue:    
        v = queue.popleft()  #큐에서 원소 하나꺼냄
        for i in gragh[v]:  #해당 원소와 인접한 노드 중
            if color[i] == 0: #아직 방문하지 않은 노드라면
                color[i] = -color[v] #색깔(집합)을 반대로 칠한다
                queue.append(i)  #큐에 추가
            elif color[i] == color[v]: #이미 방문한 노드인데 현재 노드와 같은색이라면
                return False
    return True

k = int(sys.stdin.readline()) # 테스트 케이스의 수 k 입력받음.

for _ in range(k):
    v, e = map(int, sys.stdin.readline().split()) #각 테스트 케이스 별로 정점의 수 v와 간선의 수 e를 받아옴.
    gragh = [[] for _ in range(v+1)] #각 정점마다 인접한 정점들을 저장하는 리스트 초기화.
    color = [0 for _ in range(v+1)] #해당 정점의 색깔(집합)을 저장할 리스트 초기화.

    for _ in range(e): 
        a, b = map(int, sys.stdin.readline().split()) # 간선 정보 입력받음.
        gragh[a].append(b) # 양방향 그래프이므로 a-b 연결 정보 추가.
        gragh[b].append(a) # ''

    answer = True

    for i in range(1, v+1):
        if color[i] == 0: # 아직 방문하지 않은 상태라면 BFS 탐색 시작. 
            if not bfs(i): #만약 탐색 과정에서 이분 그래프가 아니라는 결과(False)가 반환되면
                answer = False  #answer를 False로 설정
                break

    print('YES' if answer else 'NO')