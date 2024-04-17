import sys
input = sys.stdin.readline

arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
t = int(input())

for _ in range(t):
    ans = []
    w = input().rstrip()
    k = int(input())

    for alphabet in arr:
        temp = []
        for i in range(len(w)):
            if w[i] == alphabet:
                temp.append(i)
        l = len(temp)
        for j in range(l):
            if j+k <= l:
                ans.append(temp[j+k-1] - temp[j] + 1)

    if ans:
        ans.sort()
        print(ans[0], ans[-1])
    else:
        print(-1)