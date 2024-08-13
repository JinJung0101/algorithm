import sys
import heapq

def find_nth_largest(n):
    min_heap = []
    for _ in range(n):
        numbers = map(int, sys.stdin.readline().split())
        for num in numbers:
            heapq.heappush(min_heap, num)
            if len(min_heap) > n:
                heapq.heappop(min_heap)
    return min_heap[0]

n = int(sys.stdin.readline())
print(find_nth_largest(n))
