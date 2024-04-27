S = input()
P = input()

# P[i] 와 일치하는 모든 S[j] 들이 얼마나 연속되는지 조사
i = 0
s, p = len(S), len(P)
answer = 0
while i < p:
    temp = []
    for j in range(s):
        if P[i] == S[j]:
            temp.append(j)

    ans = 0
    for t in temp:
        local_ans = 0
        k = i
        while S[t] == P[k]:
            k += 1
            t += 1
            local_ans += 1
            if k == p or t == s:
                break
        if local_ans > ans:
            ans = local_ans

    i += ans
    answer += 1

print(answer)