n = int(input())
m = int(input())
loc = [*map(int, input().split())]
loc.sort()

dis = max(loc[0], n-loc[m-1])
for i in range(m-1):
    l = (loc[i+1] - loc[i]) // 2 + (loc[i+1] - loc[i]) % 2
    if l > dis:
        dis = l

print(dis)