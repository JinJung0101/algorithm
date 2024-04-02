s = input()
ans = 0
for i in range(1, len(s)+1):
    temp = dict()
    for j in range(len(s)-i+1):
        if s[j:j+i] not in temp.keys():
            temp[s[j:j+i]] = 1
            ans += 1
print(ans)