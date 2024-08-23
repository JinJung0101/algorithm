def solve_towers(N, heights):
    stack = []
    result = [0] * N
    
    for i in range(N):
        # 현재 탑의 높이가 스택의 탑 높이보다 클 때까지 스택에서 제거
        while stack and stack[-1][0] < heights[i]:
            stack.pop()
        
        # 스택이 비어 있지 않다면, 스택의 탑이 신호를 받음
        if stack:
            result[i] = stack[-1][1] + 1
        
        # 현재 탑을 스택에 추가
        stack.append((heights[i], i))
    
    return result

# 입력 처리
N = int(input())
heights = list(map(int, input().split()))

# 결과 출력
print(" ".join(map(str, solve_towers(N, heights))))
