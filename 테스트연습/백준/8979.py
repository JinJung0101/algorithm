import sys
input = sys.stdin.readline

n, k = map(int, input().split())
score = []
for _ in range(n):
    nation, gold, silver, bronze = map(int, input().split())
    score.append((gold, silver, bronze, nation))

score.sort(reverse=True)
idx = 0
g, s, b = -1, -1, -1
temp = 1
for i in range(n):
    if g == score[i][0] and s == score[i][1] and b == score[i][2]:
        temp += 1
    else:
        g, s, b = score[i][0], score[i][1], score[i][2]
        idx += temp
        temp = 1

    if score[i][3] == k:
        print(idx)
        break