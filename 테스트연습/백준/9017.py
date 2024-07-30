from collections import deque
import sys
input = sys.stdin.read

def main():
    data = input().strip().split()
    test_cases = int(data[0])
    index = 1
    
    results = []
    for _ in range(test_cases):
        n, target = map(int, data[index:index+2])
        priorities = list(map(int, data[index+2:index+2+n]))
        index += 2 + n
        
        queue = deque((priority, idx) for idx, priority in enumerate(priorities))
        count = 0
        
        while queue:
            current = queue.popleft()
            if any(current[0] < other[0] for other in queue):
                queue.append(current)
            else:
                count += 1
                if current[1] == target:
                    results.append(str(count))
                    break
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
