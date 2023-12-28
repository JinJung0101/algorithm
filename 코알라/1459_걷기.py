import sys 

x, y, w, s = map(int, sys.stdin.readline().split())

ans = 0

#가로 세로 이동
if (w * 2) < s:
    ans = (x + y) * w
else:
    #대각선으로만 이동
    if (x + y) % 2 == 0:
        if x > y:
            ans = x * s
        else:
            ans = y * s
    #대각선 + 가로세로 이동
    else:
        if x > y:
            ans = (x - 1) * s + w
        else:
            ans = (y - 1) * s + w

print(ans) 