# N = int(input())

# def tile(n):
#     cache = [0 for i in range(n+1)]
#     cache[0] = 0
#     cache[1] = 1
#     cache[2] = 2
#     for i in range(3, n + 1):
#         cache[i] = (cache[i-2] + cache[i-1])%15746
#     return cache[n]



# print(tile(N))

N = int(input())

def tile(n):
    a, b = 1, 2
    for _ in range(n-1):
        a,  b = b, (a+b)%15746
    return a



print(tile(N))
