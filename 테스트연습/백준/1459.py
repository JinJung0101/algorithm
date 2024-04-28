x, y, forward, cross = map(int, input().split())

m = min(x, y)
M = max(x, y)
if cross < forward:
    if (M-m) % 2 == 0:
        print(M * cross)
    else:
        print((M-1) * cross + forward)
elif cross < forward * 2:
    print(m * cross + (M-m) * forward)
else:
    print((m+M) * forward)