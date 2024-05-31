n = int(input())

dp = [1 for _ in range(16)]
dp[1] = 3
dp[2] = 11

for i in range(3, 16):
    dp[i] = dp[i-1] * 3
    for j in range(i-2, -1, -1):
        dp[i] += dp[j] * 2

if n%2 == 1:
    raise IndexError
else:
    print(dp[n//2])