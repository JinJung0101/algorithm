from sys import stdin

test_n = int(stdin.readline())

for i in range(test_n):
    n = int(stdin.readline())

    d = [0]*(n+1)

    for j in range (1, n+1):
        if j == 1:
            d[j] = 1
        elif j == 2:
            d[j] = 2
        elif j == 3:
            d[j] = 4
        else:    
            d[j] = d[j-1] + d[j-2] + d[j-3]

    print(d[n])



