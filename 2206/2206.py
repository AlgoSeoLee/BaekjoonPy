from sys import stdin, maxsize
from itertools import tee, chain
from heapq import heappop, heappush

def input_world(num_of_row):
    return [
        [v == '1' for v in stdin.readline().rstrip()]
        for _ in range(num_of_row)
    ]

DIRECTION = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1)
]

def finding_ways_walls(world, num_of_row, num_of_column, is_wall, x, y):
    ways = map(lambda d: (d[0] + x, d[1] + y), DIRECTION)
    ways = filter(
        lambda w:
            w[0] >= 0 and w[0] < num_of_column and
            w[1] >= 0 and w[1] < num_of_row,
        ways
    )

    ways, walls = tee(ways)

    if not is_wall:
        walls = filter(lambda w: world[w[1]][w[0]], walls)
    else:
        walls = None

    ways = filter(lambda w: not world[w[1]][w[0]], ways)
    return ways, walls

def calc_fastest_time(world, num_of_row, num_of_column):
    queue = []
    visited = [
        [
            [maxsize for _ in range(num_of_column)]
            for _ in range(num_of_row)
        ]
        for _ in range(2)
    ]

    queue.append((1, 0, 0, False))
    visited[0][0][0] = 0
    while queue:
        time, x, y, is_drilled = heappop(queue)
        next_time = time + 1

        ways, walls = finding_ways_walls(
            world, num_of_row, num_of_column, is_drilled, x, y
        )

        is_visited = (
            lambda w:
                w[0] < visited[0][w[2]][w[1]] and
                (not w[3] or w[0] < visited[1][w[2]][w[1]])
        )

        ways = map(lambda w: (next_time, w[0], w[1], is_drilled), ways)

        if not is_drilled:
            walls = map(lambda w: (next_time, w[0], w[1], True), walls)
            ways = chain(ways, walls)

        ways = filter(is_visited, ways)

        for w in ways:
            if w[1] == num_of_column - 1 and w[2] == num_of_row - 1:
                return w[0]
            visited[1 if w[3] else 0][w[2]][w[1]] = w[0]
            heappush(queue, w)

    return -1

num_of_row, num_of_column = map(int, stdin.readline().split())
world = input_world(num_of_row)

print(calc_fastest_time(world, num_of_row, num_of_column))
