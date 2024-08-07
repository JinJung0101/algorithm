def count_letters(word):
    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts

def is_similar(base_counts, word_counts):
    differences = 0
    for letter in set(base_counts.keys()).union(set(word_counts.keys())):
        diff = base_counts.get(letter, 0) - word_counts.get(letter, 0)
        if diff != 0:
            differences += abs(diff)
    # 한 글자를 변경, 추가, 또는 제거
    return differences <= 2

import sys
input = sys.stdin.read

def main():
    data = input().split()
    n = int(data[0])
    base_word = data[1]
    base_counts = count_letters(base_word)
    similar_count = 0

    for i in range(2, n+1):
        word_counts = count_letters(data[i])
        if is_similar(base_counts, word_counts):
            similar_count += 1

    print(similar_count)

if __name__ == "__main__":
    main()
