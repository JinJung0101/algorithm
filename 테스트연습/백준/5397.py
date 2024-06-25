from sys import stdin
input = stdin.read

def process_keystrokes(keystrokes):
    left_stack = []
    right_stack = []
    
    for char in keystrokes:
        if char == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif char == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(char)
    
    # left_stack과 right_stack을 합쳐서 결과를 만듭니다.
    return ''.join(left_stack) + ''.join(reversed(right_stack))

# 입력 받기
input_data = input().strip().split()
T = int(input_data[0])
results = []

for i in range(1, T + 1):
    keystrokes = input_data[i]
    result = process_keystrokes(keystrokes)
    results.append(result)

# 결과 출력
for result in results:
    print(result)
