import sys
input = sys.stdin.read

def main():
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    words = data[2:]

    word_count = {}
    for word in words:
        if len(word) >= M:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # 필터링: M번 이상 나온 단어들만 고려
    filtered_words = [word for word in word_count if word_count[word] >= M]

    # 정렬 기준: 빈도 -> 길이 -> 사전 순
    sorted_words = sorted(filtered_words, key=lambda x: (-word_count[x], -len(x), x))

    for word in sorted_words:
        print(word)

if __name__ == "__main__":
    main()
