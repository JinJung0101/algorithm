def min_string(s, delete0, delete1):
    count0 = s.count('0')
    count1 = s.count('1')

    # 실제로 삭제할 '0'과 '1'의 개수
    actual_delete0 = min(count0, delete0)
    actual_delete1 = min(count1, delete1)

    # 남은 '0'과 '1'의 개수
    remain0 = count0 - actual_delete0
    remain1 = count1 - actual_delete1

    # 결과 문자열 생성
    result = '0' * remain0 + '1' * remain1
    return result

# 입력 예시
s = input()
delete0, delete1 = map(int, input().split())
print(min_string(s, delete0, delete1))
