def manage_keywords():
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    
    n, m = map(int, data[0].split())
    keywords = set(data[1:n+1])  # 초기 키워드 목록

    results = []
    for i in range(n+1, n+1+m):
        if i >= len(data):  # 입력이 부족한 경우 예외 처리
            break
        to_delete = data[i].split(',')  # 쿼리로 주어진 키워드
        keywords.difference_update(to_delete)  # 키워드 삭제
        results.append(str(len(keywords)))  # 남은 키워드 수 출력

    return '\n'.join(results)

# 결과를 출력
print(manage_keywords())
