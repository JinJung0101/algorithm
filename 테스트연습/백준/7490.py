import copy


def dfs(idx, ar, m):
    op = [' ', '+', '-']
    for j in range(3):
        ar[idx] = op[j]
        if idx == 2 * m - 3:
            calculate(ar, m)
        else:
            dfs(idx + 2, ar, m)


def calculate(ar, m):
    global answer
    temp = m
    ans = 0
    deci = 10
    for k in range(2*m-4, -1, -2):
        if ar[k+1] == '+':
            ans += temp
            temp = ar[k]
            deci = 10
        elif ar[k+1] == '-':
            ans -= temp
            temp = ar[k]
            deci = 10
        else:
            temp = temp + ar[k]*deci
            deci *= 10
    ans += temp

    if ans == 0:
        answer.append(copy.deepcopy(ar))


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0 for _ in range(2*n-1)]
    for i in range(0, 2*n-1, 2):
        arr[i] = i//2 + 1

    answer = []
    dfs(1, arr, n)
    for a in answer:
        for aa in a:
            print(aa, end='')
        print()
    print()