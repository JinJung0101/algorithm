import sys

N = int(input())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*(N) for _ in range(N)]

for term in range(1, N):
    for start in range(N):
        if start + term == N:
            break

        dp[start][start+term] = int(1e9)

        for t in range(start, start+term):
            dp[start][start+term] = min(dp[start][start+term],
                                        dp[start][t] + dp[t+1][start+term] + nums[start][0]*nums[t][1]*nums[start+term][1])
            
print(dp[0][N-1])