from collections import deque
import sys

input = sys.stdin.read
commands = input().splitlines()
n = int(commands[0])
queue = deque()

for command in commands[1:]:
    if command.startswith('push'):
        _, x = command.split()
        queue.append(x)
    elif command == 'pop':
        print(queue.popleft() if queue else -1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        print(0 if queue else 1)
    elif command == 'front':
        print(queue[0] if queue else -1)
    elif command == 'back':
        print(queue[-1] if queue else -1)
