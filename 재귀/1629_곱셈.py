import sys

a, b, c = map(int, sys.stdin.readline().split())

a_list = [0]*b
ans = [0]*b
a_list[1] = a

for i in range(2, b):
    a_list[i] = a_list[i-1]*a_list[i-1]
    ans[i] = a_list[i]%c

print(ans[b-1])