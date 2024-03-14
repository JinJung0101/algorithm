string = list(input())
b = string.count('b')
l = len(string)
ans = 1000
for i in range(l-b):
    temp = ['a' for _ in range(i)]
    for j in range(b):
        temp.append('b')
    for k in range(l-b-i):
        temp.append('a')
    cnt = 0
    for h in range(l):
        if string[h] != temp[h]:
            cnt += 1
    if cnt//2 < ans:
        ans = cnt//2

for i in range(b):
    temp = ['b' for _ in range(i)]
    for j in range(l-b):
        temp.append('a')
    for k in range(b-i):
        temp.append('b')
    cnt = 0
    for h in range(l):
        if string[h] != temp[h]:
            cnt += 1
    if cnt//2 < ans:
        ans = cnt//2

print(ans)