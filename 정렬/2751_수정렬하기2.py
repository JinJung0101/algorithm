n =  int(input())
x = [None]*n

for i in range(n):
    x[i] = int(input())

def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

insertion_sort(x)

for i in range(n):
    print(x[i])