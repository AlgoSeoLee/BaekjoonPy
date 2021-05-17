from sys import stdin
from collections import deque
from enum import Enum

Tomato = Enum("Tomato", "RIPE UNRIPE EMPTY")

def dispensing_tomato(state):
    if state == '1':
        return Tomato.RIPE
    elif state == '0':
        return Tomato.UNRIPE
    else:
        return Tomato.EMPTY

def ripening_of_tomato(box, total_x, total_y, total_z):
    queue = deque()
    visited = []
    for z in range(total_z):
        visited.append([])
        for y in range(total_y):
            visited[z].append([False for _ in range(total_x)])
            for x in range(total_x):
                target = box[z][y][x]
                if target == Tomato.RIPE:
                    queue.append((x, y, z, 0))
                    visited[z][y][x] = True
                elif target == Tomato.EMPTY:
                    visited[z][y][x] = True

    last_lapse = 0
    while queue:
        x, y, z, lapse = queue.popleft()

        diff = []
        if x != 0:
            diff.append((-1, 0, 0))
        if x != total_x - 1:
            diff.append((1, 0, 0))
        if y != 0:
            diff.append((0, -1, 0))
        if y != total_y - 1:
            diff.append((0, 1, 0))
        if z != 0:
            diff.append((0, 0, -1))
        if z != total_z - 1:
            diff.append((0, 0, 1))

        for d in diff:
            dx = x + d[0]
            dy = y + d[1]
            dz = z + d[2]
            if not visited[dz][dy][dx]:
                visited[dz][dy][dx] = True
                last_lapse = lapse + 1
                queue.append((dx, dy, dz, last_lapse))

    yet_unripe = set()
    for z in visited:
        for y in z:
            yet_unripe = yet_unripe.union(set(y))

            if len(yet_unripe) != 1:
                break

    if len(yet_unripe) != 1 or not yet_unripe.pop():
        return -1

    return last_lapse

x, y, z = map(int, stdin.readline().split())

box = []

for tz in range(z):
    box.append([])
    for _ in range(y):
        box[tz].append(
            list(map(dispensing_tomato, stdin.readline().split())))

print(ripening_of_tomato(box, x, y, z))
