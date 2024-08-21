def can_transform(s, t):
    # 재귀적으로 역으로 문자열을 추적
    if len(t) < len(s):
        return False
    if s == t:
        return True
    
    # 'A'를 제거하는 경우
    if t[-1] == 'A' and can_transform(s, t[:-1]):
        return True
    
    # 'B'를 제거하고 뒤집는 경우
    if t[-1] == 'B' and can_transform(s, t[:-1][::-1]):
        return True
    
    return False

# 입력 받기
import sys
input = sys.stdin.read
s, t = input.split()

# 결과 출력
print(1 if can_transform(s, t) else 0)
