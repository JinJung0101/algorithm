def knapsack(weights, values, W):
    n = len(values)
    
    # dp[i][w]는 i번째 아이템까지 고려하고 배낭의 무게 제한이 w일 때의 최대 가치
    dp = [[0 for w in range(W+1)] for i in range(n+1)]

    # 모든 아이템에 대해
    for i in range(1, n+1):
        # 모든 가능한 무게에 대해
        for w in range(1, W+1):
            # 아이템 i를 배낭에 넣을 수 있다면
            if weights[i-1] <= w:
                # 아이템 i를 넣었을 때의 가치와 아이템 i를 넣지 않았을 때의 가치 중 더 큰 값으로 dp[i][w]를 갱신
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                # 아이템 i를 배낭에 넣을 수 없다면 아이템 i를 넣지 않았을 때의 가치로 dp[i][w]를 갱신
                dp[i][w] = dp[i-1][w]

    # dp[n][W]는 n개의 아이템과 배낭의 무게 제한이 W일 때의 최대 가치
    return dp[n][W]

weights = [1, 3, 4, 5]  # 각 아이템의 무게
values = [1, 4, 5, 7]   # 각 아이템의 가치
W = 7                   # 배낭의 무게 제한

print(knapsack(weights, values, W))  # 출력: 9
