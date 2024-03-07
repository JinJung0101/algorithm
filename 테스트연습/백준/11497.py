import sys

num_testcase = int(input())
def solve():
    num_woods = int(input())
    woods = list(map(int, input().split()))
    woods.sort()

    _max = -1
    for i in range(2, num_woods):
        _max = max(_max, abs(woods[i] - woods[i - 2]))
    print(_max)

for i in range(num_testcase):
    solve()