from sys import stdin, maxsize
from enum import Enum
from itertools import tee, chain
from heapq import heappop, heappush

read_int = lambda: int(stdin.readline())
read_integers = lambda: map(int, stdin.readline().split())

def input_zones(num_of_zone):
    zones = []
    for _ in range(num_of_zone):
        x1, y1, x2, y2 = read_integers()
        zone = [min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)]
        zones.append(zone)

    return zones

State = Enum("State", "safe danger death")

SIZE = 501
world = [[State.safe for _ in range(SIZE)] for _ in range(SIZE)]

def world_insert_zones(zones, state):
    for left_top_x, left_top_y , right_bottom_x, right_bottom_y in zones:
        for x in range(left_top_x, right_bottom_x + 1):
            for y in range(left_top_y, right_bottom_y + 1):
                world[y][x] = state

def world_calc_minimum_damage_for_escape():
    queue = []
    visited = [[None for _ in range(SIZE)] for _ in range(SIZE)]

    queue.append((0, 0, 0))
    visited[0][0] = 0

    DIRECTION = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ]

    while queue:
        current = heappop(queue)
        cur_loss_life, cur_x, cur_y = current

        if cur_x == 500 and cur_y == 500:
            return cur_loss_life

        ways = map(
            lambda d: (cur_loss_life, cur_x + d[0], cur_y + d[1]), DIRECTION
        )
        ways = filter(
            lambda w:
                w[1] >= 0 and w[1] < SIZE and
                w[2] >= 0 and w[2] < SIZE,
            ways
        )
        safe, danger = tee(ways)

        safe = filter(
            lambda w: world[w[2]][w[1]] == State.safe, safe
        )
        danger = filter(
            lambda w: world[w[2]][w[1]] == State.danger, danger
        )
        danger = map(lambda w: (w[0] + 1, w[1], w[2]), danger)
        ways = chain(safe, danger)

        ways = filter(
            lambda w:
                visited[w[2]][w[1]] == None or
                visited[w[2]][w[1]] > w[0],
            ways
        )

        for w in ways:
            visited[w[2]][w[1]] = w[0]
            heappush(queue, w)

    return -1

num_of_danger = read_int()
danger_zones = input_zones(num_of_danger)
world_insert_zones(danger_zones, State.danger)

num_of_death = read_int()
death_zones = input_zones(num_of_death)
world_insert_zones(death_zones, State.death)

print(world_calc_minimum_damage_for_escape())

