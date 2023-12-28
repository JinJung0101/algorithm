import sys
sys.setrecursionlimit(10**9) # 파이썬의 최대 재귀 깊이 제한을 설정합니다. (DFS가 깊은 재귀에 들어갈 수 있기 때문에 필요합니다)

def dfs(start):
    for i in tree[start]:  # 시작 노드의 모든 자식 노드들을 순회합니다.
        if parent[i] == 0:  # 해당 자식 노드의 부모가 정해지지 않았다면 
            parent[i] = start  # 부모를 현재 시작 노드로 설정하고
            dfs(i)   # 그 자식노드에서 다시 dfs를 호출합니다.

N = int(input())   # 입력으로부터 트리의 총 노드 수 N을 받습니다.
tree = [[] for _ in range(N+1)]   # 각 노드와 연결된 노드들 정보를 저장할 리스트입니다.
parent = [0 for _ in range(N+1)]   # 각 노드의 부모 정보를 저장할 리스트입니다.

for _ in range(N - 1):   # 트리는 '전체 노드 수 - 1'개의 간선으로 이루어져 있으므로 N-1번 반복합니다.
    a, b = map(int, sys.stdin.readline().split())    # 연결된 간선 정보(a, b)를 입력받습니다.
    tree[a].append(b)   # a와 b가 연결되었음을 기록하고,
    tree[b].append(a)   # 반대 방향도 마찬가지로 기록합니다.

dfs(1)     # 트리는 일반적으로 root node인 '1'번부터 탐색 시작

for i in range(2, N+1):     #(root node 제외한 나머지)
    print(parent[i])        #(각 node들에 대해 parent 출력)
