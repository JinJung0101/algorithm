import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
    sushi.append(int(input()))
arr = sushi + sushi

ans = 0
for i in range(n):
    temp = set(arr[i:i+k])
    temp.add(c)
    if len(temp) > ans:
        ans = len(temp)

print(ans)