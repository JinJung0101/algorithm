from collections import deque
n = int(input())
a, b = map(int, input().split())
k = int(input())
door = []
for _ in range(k):
    door.append(int(input()))

ans = 400
q = deque()
q.append((a, b, 0, 0))
while q:
    o1, o2, t, i = q.popleft()
    if i == k:
        if t < ans:
            ans = t
        continue
    q.append((door[i], o2, t + abs(o1 - door[i]), i + 1))
    q.append((o1, door[i], t + abs(o2 - door[i]), i + 1))
print(ans)