import sys
input = sys.stdin.readline

n = int(input())
cookie = []
for _ in range(n):
    cookie.append([*map(str, input().rstrip())])

find_heart = False
for i in range(n):
    for j in range(n):
        if cookie[i][j] == '*' and not find_heart:
            heart_x, heart_y = i+1, j
            find_heart = True

left_arm = cookie[heart_x][:heart_y].count('*')
right_arm = cookie[heart_x][heart_y+1:].count('*')
left_leg = right_leg = -1
waist = -2

for i in range(n):
    if cookie[i][heart_y-1] == '*':
        left_leg += 1
    if cookie[i][heart_y] == '*':
        waist += 1
    if cookie[i][heart_y+1] == '*':
        right_leg += 1

print(heart_x+1, heart_y+1)
print(left_arm, right_arm, waist, left_leg, right_leg)