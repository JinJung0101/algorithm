#2440 별찍기-3
# n = int(input())

# for i in range(n+1, 1,-1):
#     print("*"*i)


#2441 별찍기-4
# n = int(input())

# for i in range(n+1):
#     print(" "*i, end="")
#     print("*"*(n-i))

#print(" "*i+"*"*(n-i))

#2442 별찍기-5
# n = int(input())
# for i in range(1, n+1, 1):
#     print(" "*(n-i)+("*"*(i*2-1)))

#2443 별찍기-6
# n = int(input())
# for i in range(n, 0, -1):
#     print(" "*(n-i)+("*"*(i*2-1)))

#2444 별찍기-7
# n = int(input())
# for i in range(1, n+1, 1):
#     print(" "*(n-i)+("*"*(i*2-1)))
# for i in range(n-1, 0, -1):
#     print(" "*(n-i)+("*"*(i*2-1)))

#2445 별찍기-8
# n = int(input())
# for i in range(1, n+1, 1):
#     print(("*"*(i))+" "*((n-i)*2)+("*"*(i)))
# for i in range(n-1, 0, -1):
#     print(("*"*(i))+" "*((n-i)*2)+("*"*(i)))

#2446 별찍기-9
n = int(input())
for i in range(n, 1, -1):
    print(" "*(n-i)+("*"*(i*2-1)))
for i in range(1, n+1, 1):
    print(" "*(n-i)+("*"*(i*2-1)))
