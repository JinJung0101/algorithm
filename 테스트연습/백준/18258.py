import sys
from collections import deque
input = sys.stdin.read

def process_commands(commands):
    queue = deque()
    results = []
    
    for command in commands:
        if command.startswith('push'):
            _, num = command.split()
            queue.append(int(num))
        elif command == 'pop':
            if queue:
                results.append(queue.popleft())
            else:
                results.append(-1)
        elif command == 'size':
            results.append(len(queue))
        elif command == 'empty':
            results.append(0 if queue else 1)
        elif command == 'front':
            if queue:
                results.append(queue[0])
            else:
                results.append(-1)
        elif command == 'back':
            if queue:
                results.append(queue[-1])
            else:
                results.append(-1)

    return results

def main():
    input_data = sys.stdin.read().splitlines()
    n = int(input_data[0])
    commands = input_data[1:]
    results = process_commands(commands)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()
