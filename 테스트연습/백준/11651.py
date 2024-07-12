import sys
input = sys.stdin.read

def main():
    data = input().splitlines()
    n = int(data[0])
    points = [tuple(map(int, line.split())) for line in data[1:]]

    # 정렬: 먼저 y 좌표에 따라, 그 다음 x 좌표에 따라
    sorted_points = sorted(points, key=lambda x: (x[1], x[0]))

    # 결과 출력
    for x, y in sorted_points:
        print(x, y)

if __name__ == "__main__":
    main()
