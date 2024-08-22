def simulate(N, K, belt):
    # 로봇의 위치 정보를 관리할 리스트
    robots = [False] * N
    step = 0

    while True:
        # 벨트와 로봇 이동
        belt = belt[-1:] + belt[:-1]
        robots = [False] + robots[:-1]
        robots[-1] = False  # 마지막 위치의 로봇 내림

        # 로봇 이동
        for i in range(N-2, -1, -1):
            if robots[i] and not robots[i+1] and belt[i+1] > 0:
                robots[i], robots[i+1] = False, True
                belt[i+1] -= 1

        # 새 로봇 올리기
        if belt[0] > 0:
            robots[0] = True
            belt[0] -= 1

        # 내구도 0인 칸 수 계산
        step += 1
        if belt.count(0) >= K:
            break

    return step

N, K = map(int, input().split())
belt = list(map(int, input().split()))
print(simulate(N, K, belt))
