import sys
input = sys.stdin.read

def main():
    operations = input().strip().split('\n')[1:]
    bitset = 0
    
    results = []
    for operation in operations:
        if operation.startswith('add'):
            _, x = operation.split()
            bitset |= (1 << (int(x) - 1))
        elif operation.startswith('remove'):
            _, x = operation.split()
            bitset &= ~(1 << (int(x) - 1))
        elif operation.startswith('check'):
            _, x = operation.split()
            results.append('1' if bitset & (1 << (int(x) - 1)) else '0')
        elif operation.startswith('toggle'):
            _, x = operation.split()
            bitset ^= (1 << (int(x) - 1))
        elif operation == 'all':
            bitset = (1 << 20) - 1
        elif operation == 'empty':
            bitset = 0

    print("\n".join(results))

if __name__ == "__main__":
    main()
