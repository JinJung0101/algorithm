from collections import deque

totalDays, targetDays = map(int, input().split())
visitors = [*map(int, input().split())]
M = 0
S = sum(visitors[:targetDays])
visitors = deque(visitors)

if S > M:
    M = S
    temp = [0]
elif S == M:
    temp = []

for i in range(totalDays - targetDays):
    S -= visitors[i]
    S += visitors[i + targetDays]
    if S > M:
        M = S
        temp = [i]
    elif S == M:
        temp.append(i)

if M == 0:
    print("SAD")
else:
    print(M)
    print(len(temp))