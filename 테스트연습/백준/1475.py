def main():
    import sys
    import math
    input = sys.stdin.read().strip()
    
    # 숫자 카운트 배열
    counts = [0] * 10
    
    # 각 숫자 카운트
    for char in input:
        counts[int(char)] += 1
    
    # 6과 9의 처리
    six_nine = counts[6] + counts[9]
    counts[6] = counts[9] = math.ceil(six_nine / 2)
    
    # 필요한 세트 수는 최대 카운트
    print(max(counts))

if __name__ == "__main__":
    main()
