def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    requests = list(map(int, data[1:N+1]))
    total_budget = int(data[N+1])
    
    low, high = 0, max(requests)
    answer = 0

    if sum(requests) <= total_budget:
        print(high)
        return
    
    while low <= high:
        mid = (low + high) // 2
        current_budget = sum(min(request, mid) for request in requests)
        
        if current_budget > total_budget:
            high = mid - 1
        else:
            low = mid + 1
            answer = mid  # 최대 상한액 업데이트

    print(answer)

if __name__ == "__main__":
    main()
