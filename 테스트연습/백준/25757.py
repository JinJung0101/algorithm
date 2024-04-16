import sys
input = sys.stdin.readline

n, g = map(str, input().rstrip().split())
d = dict()
for _ in range(int(n)):
    k = input()
    d[k] = 1

players = len(d.keys())
if g == 'Y':
    print(players)
elif g == 'F':
    print(players // 2)
else:
    print(players // 3)