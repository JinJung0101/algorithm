import sys
input = sys.stdin.readline

n = int(input())
dices = []
for _ in range(n):
    dices.append([*map(int, input().split())])

ans = 0
for s in range(6):
    i, temp, bot = 0, 0, s+1
    while i < n:
        idx = dices[i].index(bot)
        if idx == 0:
            temp += max(dices[i][1], dices[i][2], dices[i][3], dices[i][4])
            bot = dices[i][5]
        elif idx == 1:
            temp += max(dices[i][0], dices[i][2], dices[i][4], dices[i][5])
            bot = dices[i][3]
        elif idx == 2:
            temp += max(dices[i][0], dices[i][1], dices[i][3], dices[i][5])
            bot = dices[i][4]
        elif idx == 3:
            temp += max(dices[i][0], dices[i][2], dices[i][4], dices[i][5])
            bot = dices[i][1]
        elif idx == 4:
            temp += max(dices[i][0], dices[i][1], dices[i][3], dices[i][5])
            bot = dices[i][2]
        else:
            temp += max(dices[i][1], dices[i][2], dices[i][3], dices[i][4])
            bot = dices[i][0]
        i += 1
    if temp > ans:
        ans = temp
print(ans)