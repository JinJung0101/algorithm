from sys import stdin

n = int(stdin.readline())

stairs = [0]
for _ in range(n):
    stairs.append(map(int, stdin.readline()))

    d = [0]*(n+1)
    d[0] = 0
    d[1] = stairs[1]

    for i in range(2, n+1):
        if i == n:
            d[i] = stairs[i] + d[i-1]
        else:
            d[i] = max(stairs[i] + d[i-1], stairs[i+1] + d[i-1])

print(d[n])
    



