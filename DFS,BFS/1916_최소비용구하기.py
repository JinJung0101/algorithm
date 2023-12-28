# A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력
import sys
import heapq

inp = sys.stdin.readline

def dijkstra(graph, start, end):
    distance = [float('inf')]*(len(graph)+1) # 각 도시의 최소비용 저장할 리스트, 처음 초기값은 무한대
    distance[start] = 0 #시작도시 비용 0으로 초기화
    heap = []  # 우선순위 큐로 사용
    heapq.heappush(heap, (0, start)) # 시작 도시부터 출발하므로 힙에 (비용, 도시) 튜플

    while heap:
        cost, node = heapq.heappop(heap) #힙에서 비용이 가장 도시 꺼낸다.

        if distance[node] < cost:  # 현재 도시까지의 비용이 이미 더 작은 경우, 무시
            continue

        for next_node, next_cost in graph[node]: # 현재 도시와 연결된 다른 도시들을 확인
            total_cost = cost + next_cost   # 다음 도시로 이동하는데 필요한 비용을 계산

            if total_cost < distance[next_node]:  # 다음 도시로 이동하는데 필요한 비용이 기존의 최소 비용보다 작을 경우 갱신
                distance[next_node] = total_cost  # 최소 비용을 갱신
                heapq.heappush(heap, (total_cost, next_node))  # 힙에 (비용, 도시) 튜플을 넣기

    return distance[end] #목적지 도시까지의 최소 비용반환
 

n = int(input()) #도시의 개수
m = int(input()) #버스의 개수

graph = [[] for _ in range(n + 1)] #도시와 버스의 연결정보 저장할 인접 리스트

# 출발도시, 도착도시, 비용을 받습니다. 
for _ in range(m):
    u, v, w = map(int, inp().split())
    graph[u].append((v,w))  # 출발 도시에서 도착 도시로 가는 버스의 정보를 인접 리스트에 추가

start, end = map(int, inp().split()) # 시작 도시와 도착 도시를 입력

print(dijkstra(graph, start, end))


