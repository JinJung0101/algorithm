# python 으로 실행하면 시간초과, pypy3 로 돌릴시 300ms
n, k = map(int, input().split())

d = 0
for i in range(1, 9):
    d += (i * (9 * (10 ** (i-1))))
    if k <= d:
        break

if k <= d:
    d -= (i * (9 * (10 ** (i-1))))
    s, e = (10 ** (i-1)), (10 ** i)
    for j in range(s, e):
        d += i
        if k <= d:
            break
    d -= i
    if j <= n:
        print(str(j)[k-d-1])
    else:
        print(-1)

else:
    if k-d == 1:
        print(1)
    elif k-d <= 9:
        print(0)
    else:
        print(-1)