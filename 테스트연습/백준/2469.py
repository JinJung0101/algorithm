import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
arr = list(map(str, input().rstrip()))
start = [chr(i+65) for i in range(n)]
temp = []
flag = 0
for i in range(k):
    radder = [*map(str, input().rstrip())]
    if radder[0] == '?':
        flag = 1
        continue
    if flag == 1:
        temp.append(radder)
    else:
        for j in range(n-1):
            if radder[j] == '-':
                start[j], start[j+1] = start[j+1], start[j]
for i in range(len(temp)-1, -1, -1):
    for j in range(n-1):
        if temp[i][j] == '-':
            arr[j], arr[j+1] = arr[j+1], arr[j]
ans = ['?' for _ in range(n-1)]
for i in range(n-1):
    if start[i] == arr[i]:
        ans[i] = '*'
for i in range(n-1):
    if start[i] == arr[i+1] and start[i+1] == arr[i]:
        ans[i] = '-'
        if i < n-2:
            ans[i+1] = '*'
if ans.count('?') > 0:
    print('x'*(n-1))
else:
    for i in range(n-1):
        print(ans[i], end='')