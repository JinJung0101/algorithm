def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])  # 수열의 길이
    sequence = list(map(int, data[1:]))  # 주어진 수열
    
    stack = []
    result = []
    current = 1
    
    for num in sequence:
        while current <= num:
            stack.append(current)
            result.append('+')
            current += 1
        if stack.pop() != num:
            print("NO")
            return
        result.append('-')
    
    print('\n'.join(result))

if __name__ == "__main__":
    main()
