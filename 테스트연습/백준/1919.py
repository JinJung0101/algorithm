from collections import Counter

def main():
    import sys
    input = sys.stdin.read
    str1, str2 = input().split()
    
    count1 = Counter(str1)
    count2 = Counter(str2)
    
    # 문자 제거 개수 계산
    remove_count = 0
    
    # 모든 문자에 대해 빈도 차이 계산
    all_chars = set(str1).union(set(str2))
    for char in all_chars:
        remove_count += abs(count1.get(char, 0) - count2.get(char, 0))
    
    print(remove_count)

if __name__ == "__main__":
    main()
