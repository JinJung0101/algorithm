def find_min_number(s):
    # 연속된 숫자가 나와야 하는 값
    num = 1
    i = 0
    while i < len(s):
        # 현재 숫자가 시작되는 부분 탐색
        if s[i].isdigit():
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            # 현재 숫자를 추출
            current_number = int(s[start:i])
            # 현재 숫자가 찾고 있는 숫자보다 크면 멈춤
            if current_number > num:
                return num
            # 찾는 숫자를 업데이트
            if current_number == num:
                num += 1
        else:
            i += 1
    return num

s = input()
print(find_min_number(s))
