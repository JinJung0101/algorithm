from collections import deque

def find_min_time(N, K):
    # 범위 설정 (0부터 100000까지)
    max_range = 100001
    visited = [False] * max_range

    # 큐 초기화
    queue = deque([(N, 0)])  # (현재 위치, 현재 시간)
    visited[N] = True

    # BFS 탐색
    while queue:
        current, time = queue.popleft()

        # 동생을 찾은 경우 현재 시간 반환
        if current == K:
            return time

        # 가능한 이동 위치 계산
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos < max_range and not visited[next_pos]:
                queue.append((next_pos, time + 1))
                visited[next_pos] = True

# 입력 받기
N, K = map(int, input().split())
print(find_min_time(N, K))
