import sys
input = sys.stdin.read

def main():
    data = input().split()
    n = int(data[0])
    expectations = list(map(int, data[1:]))
    
    # 예상 등수를 정렬
    expectations.sort()
    
    # 최소 불만도 계산
    dissatisfaction = 0
    for i in range(n):
        # 실제 등수는 1부터 시작하므로 i+1을 사용
        dissatisfaction += abs(expectations[i] - (i + 1))
    
    print(dissatisfaction)

if __name__ == "__main__":
    main()
