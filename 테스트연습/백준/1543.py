string1 = input()
string2 = input()
ans = 0
i = 0
l1, l2 = len(string1), len(string2)
while i <= l1 - l2:
    if string1[i:i+l2] == string2:
        ans += 1
        i += l2
        continue
    i += 1
print(ans)