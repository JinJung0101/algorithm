def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    x = int(data[n+1])
    
    arr.sort()  # 배열을 정렬합니다.
    
    left = 0  # 시작 포인터
    right = n - 1  # 끝 포인터
    count = 0  # 조건을 만족하는 쌍의 수
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == x:
            count += 1
            left += 1
            right -= 1
        elif current_sum < x:
            left += 1
        else:
            right -= 1
    
    print(count)

if __name__ == "__main__":
    main()
