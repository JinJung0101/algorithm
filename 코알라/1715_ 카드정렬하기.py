from sys import stdin

n = int(stdin.readline())
n_list = []
for _ in range(n):
    n_list.append(int(stdin.readline()))

n_list.sort()
cards = n_list[0]
for i in range(1,n):
    print(n_list[i])

