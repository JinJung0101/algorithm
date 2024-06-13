def min_cost_to_reach(X, Y, W, S):
    x, y = 0, 0  # 출발점 (0, 0)
    
    # 모든 직선 이동
    cost_straight = (X - x + Y - y) * W
    
    # 대각선 이동 + 직선 이동
    diagonal_steps = min(X - x, Y - y)
    remaining_steps = abs((X - x) - (Y - y))
    cost_diagonal_and_straight = diagonal_steps * S + remaining_steps * W
    
    # 대각선 이동만 사용하는 경우
    # (대각선 이동이 직선 이동 두 번보다 저렴한 경우)
    cost_diagonal_only = float('inf')
    if S < 2 * W:
        if remaining_steps % 2 == 0:
            cost_diagonal_only = max(X - x, Y - y) * S
        else:
            cost_diagonal_only = (max(X - x, Y - y) - 1) * S + W
    
    # 최소 비용 계산
    min_cost = min(cost_straight, cost_diagonal_and_straight, cost_diagonal_only)
    
    return min_cost

# 입력 받기
X, Y, W, S = map(int, input().split())
print(min_cost_to_reach(X, Y, W, S))
