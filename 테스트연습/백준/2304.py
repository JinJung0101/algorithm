import sys
input = sys.stdin.readline

n = int(input())
pillars = []
for _ in range(n):
    pillars.append([*map(int, input().split())])

pillars.sort()
temp = area = 0
for i in range(1, n):
    if pillars[i][1] >= pillars[temp][1]:
        area += (pillars[i][0] - pillars[temp][0]) * pillars[temp][1]
        temp = i

if temp != n-1:
    reverse_temp = n-1
    for i in range(n-2, temp-1, -1):
        if pillars[i][1] >= pillars[reverse_temp][1]:
            area += (pillars[reverse_temp][0] - pillars[i][0]) * pillars[reverse_temp][1]
            reverse_temp = i

area += pillars[temp][1]
print(area)