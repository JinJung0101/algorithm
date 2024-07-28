import sys

def main():
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])  # 현재 점수 수
    Nnew = int(data[1])  # 새로운 점수
    P = int(data[2])  # 순위 리스트 크기 제한
    scores = list(map(int, data[3:3+N])) if N > 0 else []

    if N >= P and Nnew <= scores[-1]:
        # 새로운 점수가 순위에 들지 못하는 경우
        print(-1)
    else:
        scores.append(Nnew)
        scores.sort(reverse=True)
        rank = scores.index(Nnew) + 1
        print(rank if rank <= P else -1)

if __name__ == "__main__":
    main()
