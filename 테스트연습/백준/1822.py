na, nb = map(int, input().split())
a = set([*map(int, input().split())])
b = set([*map(int, input().split())])

c = a - b
print(len(c))
c = list(c)
c.sort()
for i in c:
    print(i, end=' ')