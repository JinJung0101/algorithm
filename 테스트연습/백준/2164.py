from collections import deque

def main():
    import sys
    input = sys.stdin.read
    N = int(input().strip())
    
    queue = deque(range(1, N + 1))
    
    while len(queue) > 1:
        queue.popleft()  # 제일 위의 카드를 버립니다.
        queue.append(queue.popleft())  # 그 다음 카드를 빼서 제일 아래에 놓습니다.
    
    print(queue[0])  # 마지막 남은 카드를 출력합니다.

if __name__ == "__main__":
    main()
