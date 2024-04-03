home = list(map(int, input().split()))
away = list(map(int, input().split()))
flag = ans = 0
for i in range(9):
    ans += home[i]
    if ans > 0:
        flag = 1
    ans -= away[i]
flipped = 'Yes' if flag else 'No'
print(flipped)