import sys
input = sys.stdin.readline

n, k = map(int, input().split())
score = []
for _ in range(n):
    nation, gold, silver, bronze = map(int, input().split())
    score.append((gold, silver, bronze, nation))

score.sort(reverse=True)
idx = 0
g, s, b = -1, -1, -1
temp = 1
for i in range(n):
    if g == score[i][0] and s == score[i][1] and b == score[i][2]:
        temp += 1
    else:
        g, s, b = score[i][0], score[i][1], score[i][2]
        idx += temp
        temp = 1

    if score[i][3] == k:
        print(idx)
        break



# 다른 풀이 -------------------------------------------

input = sys.stdin.read

def main():
    data = input().split()
    n, k = int(data[0]), int(data[1])
    scores = []
    nation_index = {}

    index = 2
    for _ in range(n):
        nation = int(data[index])
        gold = int(data[index+1])
        silver = int(data[index+2])
        bronze = int(data[index+3])
        scores.append((gold, silver, bronze, nation))
        nation_index[nation] = (gold, silver, bronze)
        index += 4

    # 메달 수에 따라 정렬
    scores.sort(reverse=True, key=lambda x: (x[0], x[1], x[2]))

    # 순위 찾기
    rank = 1
    for i, score in enumerate(scores):
        if i > 0 and score[:3] != scores[i-1][:3]:
            rank = i + 1
        if score[3] == k:
            print(rank)
            break

if __name__ == "__main__":
    main()
