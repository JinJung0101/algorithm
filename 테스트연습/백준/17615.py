def min_moves(balls):
    n = len(balls)
    # R을 왼쪽으로 모으기
    r_left = sum(1 for i in range(n) if balls[i] == 'R')
    r_right = 0
    min_r = r_left

    for i in range(n):
        if balls[i] == 'R':
            r_left -= 1
        else:
            r_right += 1
        min_r = min(min_r, r_left + r_right)

    # B를 왼쪽으로 모으기
    b_left = sum(1 for i in range(n) if balls[i] == 'B')
    b_right = 0
    min_b = b_left

    for i in range(n):
        if balls[i] == 'B':
            b_left -= 1
        else:
            b_right += 1
        min_b = min(min_b, b_left + b_right)

    return min(min_r, min_b)

# 입력 처리
n = int(input())
balls = input().strip()

# 결과 출력
print(min_moves(balls))
