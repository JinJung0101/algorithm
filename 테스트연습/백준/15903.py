import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    cards = list(map(int, data[2:2 + N]))
    
    heapq.heapify(cards)
    
    for _ in range(M):
        first = heapq.heappop(cards)
        second = heapq.heappop(cards)
        new_card = first + second
        heapq.heappush(cards, new_card)
        heapq.heappush(cards, new_card)
    
    print(sum(cards))

if __name__ == "__main__":
    main()
