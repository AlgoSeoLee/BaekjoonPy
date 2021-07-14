from sys import stdin
from enum import Enum
from collections import deque
from itertools import tee

State = Enum("State", "Lock Open Cheese")

def input_grid(num_of_row):
    return [
        [State.Cheese if v == '1' else State.Lock
        for v in stdin.readline().split()]
        for _ in range(num_of_row)
    ]

OPS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

def calc_grid(grid, num_of_col, num_of_row, start_points):
    queue = deque()
    visited = [
        [False for _ in range(num_of_col)]
        for _ in range(num_of_row)
    ]
    found_cheese = set()

    for x, y in start_points:
        queue.append((x,y))
        visited[y][x] = True

    while queue:
        x, y = queue.popleft()

        ways = map(lambda o: (o[0] + x, o[1] + y), OPS)
        ways = filter(
            lambda w:
                w[0] >= 0 and w[0] < num_of_col and
                w[1] >= 0 and w[1] < num_of_row,
            ways
        )
        ways = filter(lambda w: not visited[w[1]][w[0]], ways)
        locked, cheese = tee(ways)
        locked = filter(lambda w: grid[w[1]][w[0]] == State.Lock, locked)
        cheese = filter(lambda w: grid[w[1]][w[0]] == State.Cheese, cheese)

        for nx, ny in locked:
            visited[ny][nx] = True
            grid[ny][nx] = State.Open
            queue.append((nx, ny))

        found_cheese = found_cheese.union(cheese)

    near_cheese_air = map(
        lambda c:
            map(lambda o: (o[0] + c[0], o[1] + c[1]), OPS),
        found_cheese
    )
    near_cheese_air = map(
        lambda c:
        len(list(filter(lambda l: grid[l[1]][l[0]] == State.Open, c))),
        near_cheese_air
    )
    deleting_cheese = zip(found_cheese, near_cheese_air)
    deleting_cheese = filter(lambda c: c[1] >= 2, deleting_cheese)
    deleting_cheese = list(map(lambda c: c[0], deleting_cheese))

    for cx, cy in deleting_cheese:
        grid[cy][cx] = State.Open


    return deleting_cheese

def simulate_grid(num_of_col, num_of_row):
    grid = input_grid(num_of_row)
    hours = 0

    start_points = [(0, 0)]

    while True:
        start_points = calc_grid(grid,num_of_col,num_of_row,start_points)
        if len(start_points) == 0:
            break

        hours += 1

    return hours

num_of_row, num_of_col = map(int, stdin.readline().split())
print(simulate_grid(num_of_col, num_of_row))

