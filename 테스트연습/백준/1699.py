n = int(input())

dp = [100 for _ in range(n+1)]
dp[0], dp[1] = 0, 1
for i in range(2, n+1):
    sqr = int(i ** 0.5)
    temp = 0
    for j in range(1, sqr+1):
        dp[i] = min(dp[i], dp[i-(j**2)]+1)

print(dp[n])