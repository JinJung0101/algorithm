n, l = map(int, input().split())
fruits = list(map(int, input().split()))
fruits.sort()
for f in fruits:
    if f <= l:
        l += 1
print(l)