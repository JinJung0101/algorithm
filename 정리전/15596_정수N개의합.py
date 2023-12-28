list = [1,2,3,4,5]

def solve(a):
    ans = 0
    for i in range(len(a)):
        ans += a[i]
    return ans

print(solve(list))
# a = 0
# for i in range(len(list)):
#     a += list[i]
# print(a)