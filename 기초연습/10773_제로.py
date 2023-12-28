import sys

n = int(sys.stdin.readline())
answer = 0
jaemin = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num > 0:
        jaemin.append(num)
    else:
        jaemin.pop()


# for i in jaemin:
#     answer += i

print(sum(jaemin))

