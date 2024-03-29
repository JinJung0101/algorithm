arr = [i for i in range(21)]
for _ in range(10):
    a, b = map(int, input().split())
    for i in range(a, (a+b+1)//2):
        arr[i], arr[b+a-i] = arr[b+a-i], arr[i]

for i in range(1, 21):
    print(arr[i], end=' ')