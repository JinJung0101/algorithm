def solve_kcpc():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])  # 테스트 케이스의 수
    idx += 1
    
    results = []
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])  # 팀의 수, 제출의 수
        idx += 2
        scores = {}
        
        for _ in range(K):
            team_id, problem_id, score, time = int(data[idx]), int(data[idx+1]), int(data[idx+2]), int(data[idx+3])
            idx += 4
            if team_id not in scores:
                scores[team_id] = (score, time)
            else:
                current_score, first_time = scores[team_id]
                if score > current_score:
                    scores[team_id] = (score, time)
                elif score == current_score and time < first_time:
                    scores[team_id] = (score, time)
        
        # 정렬 및 순위 결정
        sorted_teams = sorted(scores.items(), key=lambda x: (-x[1][0], x[1][1]))
        for rank, (team_id, (score, time)) in enumerate(sorted_teams, start=1):
            results.append(f"{team_id} {rank}")
    
    return "\n".join(results)

print(solve_kcpc())
