#무한 수열
n, p, q = map(int, input().split())

dp = dict()
n1 = n//p
n2 = n//q


def ans(n):
    if n == 0:
        return 1

    if dp.get(n//p) and dp.get(n//q):
        pass
    elif dp.get(n//p) and not dp.get(n//q):
        dp[n//q] = ans(n//q)
    elif not dp.get(n//p) and dp.get(n//q):
        dp[n//p] = ans(n//p)
    else:
        dp[n//q] = ans(n//q)
        dp[n//p] = ans(n//p)
    return dp[n//p] + dp[n//q]


print(ans(n))