import sys
input = sys.stdin.read

def can_distribute(heights, max_diff, h):
    count, current_sum = 1, 0
    for height in heights:
        if current_sum + height > max_diff:
            count += 1
            current_sum = height
            if count > h:
                return False
        else:
            current_sum += height
    return True

def main():
    data = input().split()
    m = int(data[0])
    n = int(data[1])
    h = int(data[2])
    
    heights = [0] * n
    index = 3
    for _ in range(m):
        for j in range(n):
            heights[j] += int(data[index])
            index += 1

    left, right = max(heights), sum(heights)
    while left < right:
        mid = (left + right) // 2
        if can_distribute(heights, mid, h):
            right = mid
        else:
            left = mid + 1
    
    print(left)

if __name__ == "__main__":
    main()



# 다른 풀이 ---------------------------------------------
def solve_books(n, m, h, books):
    # 책의 누적합 계산
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i-1] + books[i-1]

    # DP 배열 초기화
    inf = float('inf')
    dp = [[inf] * (h + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    # DP 점화식 적용
    for i in range(1, n + 1):
        for j in range(1, h + 1):
            for k in range(0, i):
                sum_weight = prefix_sum[i] - prefix_sum[k]
                dp[i][j] = min(dp[i][j], max(dp[k][j-1], sum_weight))

    # 최소 최대 무게 합 출력
    return dp[n][h]

# 입력 처리
m, n, h = map(int, input().split())
books = [0] * n
for _ in range(m):
    weights = list(map(int, input().split()))
    for i in range(n):
        books[i] += weights[i]

# 결과 출력
print(solve_books(n, m, h, books))
