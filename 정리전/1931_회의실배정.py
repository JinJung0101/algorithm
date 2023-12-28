import sys

n = int(sys.stdin.readline())

n_schedule = []
for i in range(n):
    n_schedule.append(list(map(int, sys.stdin.readline().split())))

n_schedule.sort(key=lambda x: (x[1],x[0]))

count = 1
end_time = n_schedule[0][1]

for i in range(1, n):
    if n_schedule[i][0] >= end_time:
        count += 1
        end_time = n_schedule[i][1]

        
print(count)
