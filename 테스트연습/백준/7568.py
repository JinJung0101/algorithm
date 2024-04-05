import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    kg, cm = map(int, input().split())
    arr.append((kg, cm))

for i in range(n):
    temp = 1
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            temp += 1
    print(temp, end=' ')