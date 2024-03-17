n = int(input())
if n == 2:
    print('CY')
elif n == 1 or n == 3:
    print('SK')
else:
    dp = ['CY' for _ in range(n+1)]
    dp[1] = dp[3] = dp[4] = 'SK'
    for i in range(1, n+1):
        if dp[i] == 'CY':
            if i+1 <= n:
                dp[i+1] = 'SK'
            if i+3 <= n:
                dp[i+3] = 'SK'
            if i+4 <= n:
                dp[i+4] = 'SK'
    print(dp[n])