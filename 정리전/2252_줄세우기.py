# 위상정렬(graph)
# 1. 입력: 방향 그래프 graph
# 2. 출력: 노드의 리스트

# 1. 모든 노드에 대해 진입 차수를 계산한다.
# 2. 진입 차수가 0인 모든 노드를 큐에 넣는다.
# 3. 큐가 비어있지 않은 동안 다음의 단계를 반복한다.
#     1) 큐에서 노드 n을 꺼낸다.
#     2) n을 결과 리스트에 추가한다.
#     3) n에서 나가는 모든 간선 e를 그래프에서 제거한다.
#     4) e의 목표노드의 진입차수가 0이라면 그 노드를 큐에 넣는다.
# 4. 모든 노드가 결과 리스트에 들어있다면, 그 리스트를 반환한다.
# 5. 결과 리스트의 길이와 그래프의 노드 수가 다르다면, 그래프에 사이클이 존재하는 것으로 에러를 반환한다.
from collections import deque
import sys

inp = sys.stdin.readline

n, m = map(int, inp().split())
indegree = [0] * (n+1) #각 노드의 진입차수를 저장할 리스트
graph= [[] for _ in range(n+1)] #각 노드의 간선 정보를 저장할 리스트

# 간선 정보를 입력받아 그래프를 완성하고 진입차수를 계산
for _ in range(m):
    a, b = map(int, inp().split()) # 간선 정보를 입력받음
    graph[a].append(b) # a 노드에서 출발하는 간선 정보를 그래프에 추가
    indegree[b] += 1 # b 노드의 진입차수를 1 증가

def topological_sort():
    result = [] #위상정렬 결과를 담을 리스트
    queue = deque() #진입차수가 0인 노드를 담을 큐

    #진입차수가 0인 노드를 큐에 추가
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        v = queue.popleft() #큐에서 노드를 꺼냄
        result.append(v) #결과 리스트에 추가
        #해당 노드와 연결된 노드의 진입차수를 1감소
        for i in graph[v]:
            indegree[i] -= 1
            #진입차수가 0이 된 노드를 큐에 추가
            if indegree[i] == 0:
                queue.append(i)

    return result

topo_result = topological_sort() #위상정렬 수행

for i in topo_result:
    print(i, end=' ')