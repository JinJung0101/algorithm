from collections import deque

n=int(input()) #컴퓨터 개수
v=int(input()) #연결선 개수

graph = [[] for i in range(n+1)]#그래프 초기화, 1번 컴퓨터를 1번 인덱스를 쓰기 위해, 1개 더 추가
visited = [0]*(n+1) # 방문한 컴퓨터인지 표시 (0: 미방문, 1: 방문)

for i in range(v): #그래프 생성
    a, b = map(int, input().split())
    graph[a]+=[b]
    graph[b]+=[a] #양방향 연결

visited[1]=1 #1번 컴퓨터부터 시작이니 방문 표시

Q = deque([1]) #첫번째 컴퓨터에 대해 덱을 만든다.
while Q:
    c = Q.popleft() # c= 현재 컴퓨터
    for nx in graph[c]: #nx= next
        if visited[nx]==0: # nx 컴퓨터가 방문되지 않은 컴퓨터라면, visited[nx]==0가 참
            Q.append(nx)
            visited[nx]=1

print(sum(visited)-1) # 1번 컴퓨터를 제외하고 출력