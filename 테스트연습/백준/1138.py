n = int(input())
arr = [*map(int, input().split())]
arr2 = [-1 for _ in range(n)]
for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == arr[i] and arr2[j] == -1:
            arr2[j] = i+1
            break
        if arr2[j] == -1:
            cnt += 1
for i in arr2:
    print(i, end=' ')