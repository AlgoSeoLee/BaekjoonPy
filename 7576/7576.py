from sys import stdin
from collections import deque
from enum import Enum

"https://www.acmicpc.net/problem/7576 토마토 <Silver I>"

Tomato = Enum("Tomato", "RIPE UNRIPE EMPTY")

def dispensing_tomato(state):
    if state == '1':
        return Tomato.RIPE
    elif state == '0':
        return Tomato.UNRIPE
    else:
        return Tomato.EMPTY

def ripening_of_tomato(box, total_x, total_y):
    queue = deque()
    visited = [[False for _ in range(total_x)] for _ in range(total_y)]

    for y in range(total_y):
        for x in range(total_x):
            if box[y][x] == Tomato.RIPE:
                queue.append((x, y, 0))
                visited[y][x] = True
            elif box[y][x] == Tomato.EMPTY:
                visited[y][x] = True

    last_lapse = 0
    try:
        while True:
            x, y, lapse = queue.popleft()
    
            diff = []
            if x != 0:
                diff.append((-1, 0))
            if x != total_x - 1:
                diff.append((1, 0))
            if y != 0:
                diff.append((0, -1))
            if y != total_y - 1:
                diff.append((0, 1))
    
            for d in diff:
                dx = x + d[0]
                dy = y + d[1]
                if not visited[dy][dx] and box[dy][dx] == Tomato.UNRIPE:
                    visited[dy][dx] = True
                    box[dy][dx] = Tomato.RIPE
                    last_lapse = lapse + 1
                    queue.append((dx, dy, last_lapse))
    except IndexError:
        pass

    yet_unripe = set()
    for y in visited:
        yet_unripe = yet_unripe.union(set(y))

        if len(yet_unripe) != 1:
            break

    if len(yet_unripe) != 1 or not yet_unripe.pop():
        return -1

    return last_lapse

x, y = map(int, stdin.readline().split())

box = []

for _ in range(y):
    box.append(list(map(dispensing_tomato, stdin.readline().split())))

print(ripening_of_tomato(box, x, y))
