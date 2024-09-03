# bisect.bisect_left: 주어진 점수 리스트에서 Nnew가 들어갈 위치를 찾습니다. 여기서 key=lambda x: -x는 점수를 내림차순으로 처리하기 위해 사용됩니다.
# insert_pos: 새로운 점수가 삽입될 위치입니다.
# 리스트에 새로운 점수를 삽입한 후, 해당 점수의 순위(위치+1)를 계산합니다.
# 만약 순위가 순위 리스트의 크기 제한 P를 초과한다면 -1을 출력합니다.

import sys
import bisect

def main():
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])  # 현재 점수 수
    Nnew = int(data[1])  # 새로운 점수
    P = int(data[2])  # 순위 리스트 크기 제한
    scores = list(map(int, data[3:3+N])) if N > 0 else []

    # 순위 리스트가 이미 가득 찼고, 새로운 점수가 리스트의 최소 점수보다 작거나 같은 경우
    if N >= P and (Nnew <= min(scores)):
        print(-1)
        return

    # 새로운 점수를 정렬된 리스트에 적절한 위치에 삽입
    insert_pos = bisect.bisect_left(scores, Nnew, key=lambda x: -x)

    # 새로운 점수를 리스트에 추가
    scores.insert(insert_pos, Nnew)

    # 순위 계산
    rank = scores.index(Nnew) + 1

    # 순위가 P를 넘어가면 출력하지 않음
    if rank > P:
        print(-1)
    else:
        print(rank)

if __name__ == "__main__":
    main()
