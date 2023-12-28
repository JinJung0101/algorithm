import networkx as nx

# 그래프 생성
G = nx.Graph()

# 정점 추가
G.add_nodes_from([1, 2, 3, 4, 5, 6])

# 간선 추가
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 5), (5, 6)])

# 그래프 시각화
import matplotlib.pyplot as plt
nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
plt.show()

# DFS(깊이 우선 탐색) 알고리즘
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

print("DFS 탐색 결과:")
dfs(G, 1)
print()

# BFS(너비 우선 탐색) 알고리즘
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

print("BFS 탐색 결과:")
bfs(G, 1)
