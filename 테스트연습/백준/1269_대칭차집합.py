import sys

a, b = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

ans1 = list(set(A) - set(B))
ans2 = list(set(B) - set(A))
print(len(ans1)+len(ans2))
