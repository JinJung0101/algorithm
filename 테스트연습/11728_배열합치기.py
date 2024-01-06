import sys

a, b = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
ans = sorted(A + B)
# for i in ans:
#     print(i, end=' ')
# print가 너무 많이 호출되어 속도가 느리다.
print(' '.join(map(str, ans)))