from collections import deque

n, k = map(int, input().split())

if n >= k:
    print(n-k)
    for i in range(n, k-1, -1):
        print(i, end=' ')
else:
    R = 100001
    route = [-1 for _ in range(R+1)]
    q = deque([(n, 0)])

    while q:
        loc, cos = q.popleft()

        if loc == k:
            print(cos)

            answer = [k]
            temp = k
            while temp != n:
                answer.append(route[temp])
                temp = route[temp]
            for i in range(len(answer)-1, -1, -1):
                print(answer[i], end=' ')
            break

        if R >= loc-1 >= 0 and route[loc-1] == -1:
            q.append((loc-1, cos+1))
            route[loc-1] = loc
        if R >= loc+1 >= 0 and route[loc+1] == -1:
            q.append((loc+1, cos+1))
            route[loc+1] = loc
        if R >= 2*loc >= 0 and route[2*loc] == -1:
            q.append((2*loc, cos+1))
            route[2*loc] = loc