import sys

def main():
    input = sys.stdin.read().strip()
    word = input.upper()  # 입력 단어를 대문자로 변환
    freq = [0] * 26  # 알파벳 빈도 배열

    # 문자 빈도 계산
    for char in word:
        index = ord(char) - ord('A')
        freq[index] += 1

    # 최대 빈도와 그 알파벳 찾기
    max_freq = max(freq)
    if freq.count(max_freq) > 1:
        print('?')
    else:
        max_index = freq.index(max_freq)
        print(chr(max_index + ord('A')))

if __name__ == "__main__":
    main()


# 다른풀이 ------------------------------
import sys
from collections import Counter

def main():
    input = sys.stdin.read().strip().upper()  # 입력 단어를 대문자로 변환
    freq = Counter(input)  # 문자 빈도 계산

    # 가장 많이 등장하는 문자 찾기
    max_freq = max(freq.values())
    # 최대 빈도의 문자 리스트
    max_chars = [char for char, count in freq.items() if count == max_freq]

    # 최대 빈도의 문자가 여러 개 있는 경우 '?' 출력, 아니면 해당 문자 출력
    if len(max_chars) > 1:
        print('?')
    else:
        print(max_chars[0])

if __name__ == "__main__":
    main()
