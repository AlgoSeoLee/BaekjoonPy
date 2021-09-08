from sys import stdin, maxsize
from itertools import tee, chain
from collections import deque

"https://www.acmicpc.net/problem/2206 벽 부수고 이동하기 <Gold IV>"

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

def calc_fastest_time(world, num_of_row, num_of_column):
    if num_of_row == 1 and num_of_column == 1:
        return 1

    queue = deque()
    visited = [
        [
            [maxsize for _ in range(num_of_column)]
            for _ in range(num_of_row)
        ]
        for _ in range(2)
    ]

    is_range = (
        lambda w:
            w[0] >= 0 and w[0] < num_of_column and
            w[1] >= 0 and w[1] < num_of_row
    )
    is_visited = (
        lambda w:
            w[0] < visited[0][w[2]][w[1]] and
            (not w[3] or w[0] < visited[1][w[2]][w[1]])
    )

    queue.append((1, 0, 0, False))
    visited[0][0][0] = 0
    while queue:
        time, x, y, is_drilled = queue.pop()
        next_time = time + 1

        ways = map(lambda d: (d[0] + x, d[1] + y), DIRECTION)
        ways = filter(is_range, ways)

        ways = filter(
            lambda w:
                not world[w[1]][w[0]] or
                (not is_drilled and world[w[1]][w[0]]),
            ways
        )

        ways = map(
            lambda w:
                (next_time, w[0], w[1], is_drilled or world[w[1]][w[0]]),
            ways
        )

        ways = filter(is_visited, ways)

        for w in ways:
            if w[1] == num_of_column - 1 and w[2] == num_of_row - 1:
                return w[0]
            visited[1 if w[3] else 0][w[2]][w[1]] = w[0]
            queue.appendleft(w)

    return -1

num_of_row, num_of_column = map(int, stdin.readline().split())
world = input_world(num_of_row)

print(calc_fastest_time(world, num_of_row, num_of_column))
