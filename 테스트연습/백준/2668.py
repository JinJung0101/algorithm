import sys
input = sys.stdin.readline

n = int(input())
card = [0]
for _ in range(n):
    card.append(int(input()))

ans = []
for i in range(1, n+1):
    temp = []
    j = i
    flag = 0
    while 1:
        if card[j] == i:
            flag = 1
            break
        if card[j] in temp:
            break
        temp.append(card[j])
        j = card[j]
    if flag:
        ans.append(i)

print(len(ans))
for t in ans:
    print(t)