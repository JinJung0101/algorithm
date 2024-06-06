def create_maze(commands):
    # 초기 설정
    direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 남, 서, 북, 동
    current_direction = 0
    x, y = 0, 0
    path = [(x, y)]

    # 명령어 수행
    for command in commands:
        if command == 'F':
            x += direction[current_direction][0]
            y += direction[current_direction][1]
            path.append((x, y))
        elif command == 'L':
            current_direction = (current_direction - 1) % 4
        elif command == 'R':
            current_direction = (current_direction + 1) % 4

    # 미로의 크기 계산
    min_x = min(x for x, y in path)
    max_x = max(x for x, y in path)
    min_y = min(y for x, y in path)
    max_y = max(y for x, y in path)

    # 미로 배열 초기화
    maze = [['.' for _ in range(min_y, max_y + 1)] for _ in range(min_x, max_x + 1)]

    # 경로를 미로에 표시
    for x, y in path:
        maze[x - min_x][y - min_y] = '#'

    # 미로 출력
    for row in maze:
        print(''.join(row))


commands = "FLFLFRF"
create_maze(commands)
