# 종이접을때의 절반을 기준으로 양옆이 반대
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    p = input().rstrip()
    l = len(p)

    TorF = True
    test = l//2
    while test > 0:
        if not TorF:
            break
        i = 1
        while i <= test:
            if p[test+i] == p[test-i]:
                TorF = False
                break
            if p[l-test-1+i] == p[l-test-1-i]:
                TorF = False
                break
            i += 1
        test //= 2

    if TorF:
        print("YES")
    else:
        print("NO")