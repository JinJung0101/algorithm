def distribute_burgers(line, k):
    n = len(line)
    burgers = [i for i in range(n) if line[i] == 'H']
    people = [i for i in range(n) if line[i] == 'P']
    used = [False] * len(burgers)
    count = 0
    
    for person in people:
        for i in range(len(burgers)):
            if not used[i] and abs(burgers[i] - person) <= k:
                used[i] = True
                count += 1
                break

    return count

# 입력 받기
import sys
input = sys.stdin.read
data = input().split()
n, k = int(data[0]), int(data[1])
line = data[2]

# 결과 출력
print(distribute_burgers(line, k))
