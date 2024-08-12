def group_players(players, p):
    groups = []
    players.sort()  # 레벨에 따라 플레이어 정렬

    for level, name in players:
        placed = False
        for group in groups:
            if group['min_level'] <= level <= group['max_level'] and len(group['players']) < p:
                group['players'].append(name)
                placed = True
                break
        if not placed:
            groups.append({
                'min_level': max(1, level - 10),
                'max_level': level + 10,
                'players': [name]
            })

    for group in sorted(groups, key=lambda x: x['players']):
        print(' '.join(sorted(group['players'])))

# 입력 받기
n, p = map(int, input().split())
players = []
for _ in range(n):
    level, name = input().split()
    players.append((int(level), name))

group_players(players, p)
