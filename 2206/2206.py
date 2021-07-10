from sys import stdin
from collections import deque

def calc_fastest_way(world, total_x, total_y, start_x, start_y):
    # 변수 초기화
    visited = {}
    visited[(start_y,start_x)] = 1
    queue = deque()
    queue.append((start_x, start_y, 1))
    # 벽들을 저장할 변수
    walls = []

    # 목표 지점은 해당 지도의 x,y 최대값
    target_x = total_x - 1
    target_y = total_y - 1

    # 검사범위: 상하좌우
    diff = [
        (1, 0),
        (0, 1),
        (0, -1),
        (-1, 0),
    ]

    # BFS
    finding_wall = True
    limit = 1000001
    result = limit
    is_wall = lambda w: world[w[1]][w[0]]
    while finding_wall or queue:
        if finding_wall and not queue:
            queue.extend(walls)
            finding_wall = False
        x, y, level = queue.popleft()
        if x == target_x and y == target_y:
            if level < result:
                result = level
            continue

        # 실제 좌표값으로 변환
        ways = map(lambda d: (x + d[0], y + d[1]), diff)
        # 범위 제한
        ways = filter(
            lambda w:
                w[0] >= 0 and w[0] < total_x and
                w[1] >= 0 and w[1] < total_y,
            ways)
        # 변수 추가
        next_level = level + 1
        ways = list(map(
            lambda w:
                (w[0], w[1], next_level),
            ways))
        # 벽인지 확인, 벽이면 벽을 찾는지 확인하고 저장
        if finding_wall:
            walls.extend(filter(lambda w: is_wall(w), ways))
        ways = filter(lambda w: not is_wall(w), ways)
        # 중복 방지
        ways = filter(
            lambda w: not visited.get((w[1],w[0])) or
                next_level < visited.get((w[1],w[0])),
            ways)

        for w in ways:
            wx = w[0]
            wy = w[1]
            # 방문 등록
            visited[(w[1],w[0])] = next_level
            queue.append(w)

    if result == limit:
        return -1
    return result

def input_world(total_y):
    world = [
        [v == '1' for v in stdin.readline().rstrip()]
        for _ in range(total_y)
    ]
    return world

total_y, total_x = map(int, stdin.readline().split())
world = input_world(total_y)

print(calc_fastest_way(world, total_x, total_y, 0, 0))

