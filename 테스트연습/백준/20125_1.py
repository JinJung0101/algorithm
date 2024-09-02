# 함수 분리: 각 신체 부위의 길이를 계산하는 로직을 별도의 함수로 분리하여, 각 함수가 하나의 작업만 수행하도록 합니다.
# 직관적인 순회: 심장을 찾은 후, 심장 위치를 기준으로 상, 하, 좌, 우를 순회하는 구조로 로직을 개선합니다.

import sys
input = sys.stdin.read

def find_heart(cookie, n):
    for i in range(n):
        for j in range(n):
            if cookie[i][j] == '*' and cookie[i+1][j] == 'o':
                return i+1, j

def count_stars(cookie, n, x, y, dx, dy):
    length = 0
    while 0 <= x < n and 0 <= y < n and cookie[x][y] == '*':
        length += 1
        x += dx
        y += dy
    return length

def measure_body(cookie, n, heart_x, heart_y):
    left_arm = count_stars(cookie, n, heart_x, heart_y-1, 0, -1)
    right_arm = count_stars(cookie, n, heart_x, heart_y+1, 0, 1)
    waist = count_stars(cookie, n, heart_x+1, heart_y, 1, 0) - 1
    left_leg = count_stars(cookie, n, heart_x+waist+1, heart_y-1, 1, 0)
    right_leg = count_stars(cookie, n, heart_x+waist+1, heart_y+1, 1, 0)
    return left_arm, right_arm, waist, left_leg, right_leg

def main():
    data = input().split()
    n = int(data[0])
    cookie = [list(data[i + 1]) for i in range(n)]

    heart_x, heart_y = find_heart(cookie, n)
    left_arm, right_arm, waist, left_leg, right_leg = measure_body(cookie, n, heart_x, heart_y)
    
    print(heart_x+1, heart_y+1)
    print(left_arm, right_arm, waist, left_leg, right_leg)

if __name__ == "__main__":
    main()
