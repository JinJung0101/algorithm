import sys
input = sys.stdin.read

def main():
    data = input().split()
    n = int(data[0])
    distances = list(map(int, data[1:n]))
    prices = list(map(int, data[n:2*n-1]))
    
    # 최소 비용 계산
    min_cost = 0
    current_price = prices[0]
    
    for i in range(n-1):
        if prices[i] < current_price:
            current_price = prices[i]
        min_cost += current_price * distances[i]
    
    print(min_cost)

if __name__ == "__main__":
    main()
