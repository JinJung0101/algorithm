n, m = map(int, input().split())
arr = [*map(int, input().split())]

arr.sort()
ans = 0
for i in range(0, n, m):
    if arr[i] > 0:
        break
    ans += 2 * abs(arr[i])

for i in range(n-1, -1, -m):
    if arr[i] < 0:
        break
    ans += 2 * arr[i]

if abs(arr[0]) > abs(arr[n-1]):
    ans -= abs(arr[0])
else:
    ans -= abs(arr[n-1])

print(ans)