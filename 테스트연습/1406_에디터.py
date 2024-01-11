import sys
# list를 사용하는 예시, 시간 복잡도 O(n)
# strings = list(map(str, sys.stdin.readline().strip()))
# num = int(sys.stdin.readline())
# cursur = len(strings)
# for i in range(num):
#     temp = sys.stdin.readline().strip()
#     if temp[0] == "L":
#         if cursur == 0:
#             continue
#         else:
#             cursur -= 1
#     elif temp[0] == "D":
#         if cursur == len(strings):
#             continue
#         else:
#             cursur += 1
#     elif temp[0] == "B":
#         if cursur == 0:
#             continue
#         else:
#             strings.pop(cursur-1)
#             cursur -= 1
#     elif temp[0] == "P":
#         strings.insert(cursur, temp[2])
#         cursur += 1

# print(''.join(strings))

left_stack = list(sys.stdin.readline().strip())
right_stack = []
num = int(sys.stdin.readline())
for _ in range(num):
    temp = sys.stdin.readline().strip()
    if temp[0] == "L":
        if left_stack:
            right_stack.append(left_stack.pop())
    elif temp[0] == "D":
        if right_stack:
            left_stack.append(right_stack.pop())
    elif temp[0] == "B":
        if left_stack:
            left_stack.pop()
    elif temp[0] == "P":
        left_stack.append(temp[2])

right_stack.reverse()
print(''.join(left_stack + right_stack))



