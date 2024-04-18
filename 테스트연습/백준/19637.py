import sys
input = sys.stdin.readline

n, m = map(int, input().split())
title = []
for _ in range(n):
    name, strength = map(str, input().split())
    title.append((int(strength), name))

for _ in range(m):
    STR = int(input())
    s, e = 0, n-1
    TITLE = title[n-1][1]
    while s < e:
        m = (s + e) // 2
        if STR <= title[m][0]:
            e = m
            TITLE = title[m][1]
        else:
            s = m + 1
    print(TITLE)