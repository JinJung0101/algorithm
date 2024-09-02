#dp사용

def min_time(n, k):
    if n >= k:
        return n - k
    
    dp = [float('inf')] * 100001
    dp[n] = 0
    queue = [n]
    
    while queue:
        current = queue.pop(0)
        
        if current * 2 <= 100000 and dp[current * 2] > dp[current]:
            dp[current * 2] = dp[current]
            queue.append(current * 2)
        
        for next_pos in [current - 1, current + 1]:
            if 0 <= next_pos <= 100000 and dp[next_pos] > dp[current] + 1:
                dp[next_pos] = dp[current] + 1
                queue.append(next_pos)
                
    return dp[k]

n, k = map(int, input().split())
print(min_time(n, k))
