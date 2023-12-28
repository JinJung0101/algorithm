# case = int(input())
# nums = list(map(int, input()))

nums = [1,3,5,7,4,11,12,54,66,88,87]
answer = 0


for i in nums:
    no_ans = 0
    if i>1:
        for j in range(2, i):
            if i%j==0:
                no_ans +=1
        if no_ans ==0:
            answer +=1

print(answer)