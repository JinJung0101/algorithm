# n = int(stdin.readline())
n = int(input())

# words = [str(stdin.readline()) for i in range(n)]
words = [str(input()) for i in range(n)]

set_words = list(set(words))

set_words.sort()
set_words.sort(key = len)

for i in set_words:
    print(i)
