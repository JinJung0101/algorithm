import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    stock = [*map(int, input().split())]
    ans = 0
    M = stock[-1]

    for i in range(n-2, -1, -1):
        if stock[i] > M:
            M = stock[i]
            continue
        ans += M - stock[i]

    print(ans)