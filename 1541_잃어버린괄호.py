A = input().split("-")
answer = 0

for i in A[0].split("+"):
    answer += int(i)

for i in A[1:]:
    for j in i.split("+"):
        answer -= int(j)

print(answer)