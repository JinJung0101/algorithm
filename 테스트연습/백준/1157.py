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
