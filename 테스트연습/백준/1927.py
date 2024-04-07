n = int(input())
taller = [0] + [*map(int, input().split())]
lined = [0 for _ in range(n+1)]

for i in range(1, n+1):
    t = taller[i]
    p = 0
    for j in range(1, n+1):
        if p == t and lined[j] == 0:
            lined[j] = i
            break
        elif lined[j] == 0:
            p += 1

for i in range(1, n+1):
    print(lined[i], end=' ')