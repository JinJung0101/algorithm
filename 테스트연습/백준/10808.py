# 입력 받기
s = input().strip()

# 알파벳 개수를 저장할 배열 초기화 (a-z까지 26개)
alphabet_count = [0] * 26

# 문자열 순회하며 알파벳 개수 세기
for char in s:
    index = ord(char) - ord('a')  # 알파벳 'a'를 0으로 맞추기
    alphabet_count[index] += 1

# 결과 출력
print(" ".join(map(str, alphabet_count)))
