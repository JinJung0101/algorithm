def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])  # 로그의 수
    log_dict = {}  # 해시 테이블
    
    for line in data[1:]:
        name, status = line.split()
        if status == 'enter':
            log_dict[name] = True
        elif status == 'leave':
            del log_dict[name]
    
    # 해시 테이블에 남아있는 이름들을 역순으로 정렬
    remaining_people = sorted(log_dict.keys(), reverse=True)
    
    # 결과 출력
    for person in remaining_people:
        print(person)

if __name__ == "__main__":
    main()
