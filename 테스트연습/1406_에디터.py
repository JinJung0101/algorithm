import sys
strings = list(map(str, sys.stdin.readline().strip()))
num = int(sys.stdin.readline())
cursur = len(strings)
for i in range(num):
    temp = sys.stdin.readline().strip()
    if temp[0] == "L":
        if cursur == 0:
            continue
        else:
            cursur -= 1
    elif temp[0] == "D":
        if cursur == len(strings):
            continue
        else:
            cursur += 1
    elif temp[0] == "B":
        if cursur == 0:
            continue
        else:
            strings.pop(cursur-1)
            cursur -= 1
    elif temp[0] == "P":
        strings.insert(cursur, temp[2])
        cursur += 1

print(''.join(strings))


