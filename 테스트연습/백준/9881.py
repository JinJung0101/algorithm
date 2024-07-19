import heapq
import sys
input = sys.stdin.read

def main():
    data = input().split()
    N = int(data[0])
    heights = [list(map(int, data[1 + i*N:1 + (i+1)*N])) for i in range(N)]

    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 최대 고도 차를 저장할 배열
    max_diff = [[float('inf')] * N for _ in range(N)]
    max_diff[0][0] = 0

    # 우선순위 큐 (최소 힙)
    pq = [(0, 0, 0)]  # (고도 차, x, y)

    while pq:
        diff, x, y = heapq.heappop(pq)
        
        if x == N-1 and y == N-1:
            print(diff)
            return
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                new_diff = max(diff, abs(heights[nx][ny] - heights[x][y]))
                if new_diff < max_diff[nx][ny]:
                    max_diff[nx][ny] = new_diff
                    heapq.heappush(pq, (new_diff, nx, ny))

if __name__ == "__main__":
    main()
