t = int(input())
for _ in range(t):
    n = int(input())
    dp = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        dp[i] = dp[i] + dp[i-2]
    for j in range(3, n+1):
        dp[j] = dp[j] + dp[j-3]
    print(dp[-1])