def solve(n, m, grid):
    # DP table [n][m][3]
    dp = [[[float('inf')] * 3 for _ in range(m)] for __ in range(n)]
    
    # 초기화
    for j in range(m):
        for d in range(3):
            dp[0][j][d] = grid[0][j]

    # 가능한 이동 방향
    directions = [(-1, -1), (-1, 0), (-1, 1)]  # 좌하, 하, 우하

    # DP 진행
    for i in range(1, n):
        for j in range(m):
            for d in range(3):
                for k, (di, dj) in enumerate(directions):
                    if d == k: continue  # 같은 방향으로 연속해서 이동할 수 없음
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        dp[i][j][d] = min(dp[i][j][d], dp[ni][nj][k] + grid[i][j])

    # 결과 계산
    min_cost = float('inf')
    for j in range(m):
        for d in range(3):
            min_cost = min(min_cost, dp[n-1][j][d])
    
    return min_cost

# 입력
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(solve(n, m, grid))
