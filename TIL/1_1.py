n, k = map(int, input().split())

numbers = []
for i in range(1, n+1):
    if n % i == 0:
        numbers.append(i)
if len(numbers) < k:
    print(-1)
else:
    print(numbers[k-1])



n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)