n = int(input())
chain = [*map(int, input().split())]
chain.sort()

temp, ans, idx = 0, 0, 0
for i in range(1, n):
    if temp == chain[idx]:
        idx += 1
        temp = 0
    else:
        temp += 1
        ans += 1

print(ans)