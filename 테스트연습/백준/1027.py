n = int(input())
apart = [*map(int, input().split())]
building = 0
answer = 0
for i in range(n):
    ans = 0
    line1, line2 = 1e9, -1e9
    for j in range(i-1, -1, -1):
        x, y = i-j, apart[i]-apart[j]
        if (y/x) < line1:
            ans += 1
            line1 = (y/x)
    for k in range(i+1, n):
        x, y = k-i, apart[k]-apart[i]
        if (y/x) > line2:
            ans += 1
            line2 = (y/x)
    if ans > answer:
        answer = ans
print(answer)