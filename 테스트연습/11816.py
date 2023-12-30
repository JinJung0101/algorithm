num = str(input())

if num.startswith('0'):
    if 'x' in num:
        print(int(num, 16))
    else:
        print(int(num, 8))
else:
    print(int(num, 0))

