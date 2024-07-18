def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    n = data[0]  # 학생의 수는 2n
    abilities = data[1:]  # 능력치 배열
    
    abilities.sort()  # 능력치 정렬
    min_max_team_ability = float('inf')  # 최소 팀 능력치의 최대값 초기화
    
    # 양 끝에서부터 팀을 만들어 능력치 계산
    for i in range(n):
        team_ability = abilities[i] + abilities[2*n - 1 - i]
        if team_ability < min_max_team_ability:
            min_max_team_ability = team_ability
    
    print(min_max_team_ability)  # 최소 팀 능력치의 최대값 출력

if __name__ == "__main__":
    main()
