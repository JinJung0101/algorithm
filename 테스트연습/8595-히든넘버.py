n = int(input())
text = list(input())
nums = set('0123456789')
ans = []
for t in text:
    if t in nums:
        ans.append(t)
    else:
        ans.append(' ')

print(sum(list(map(int, ''.join(ans).split()))))