from sys import stdin
from collections import deque

"https://www.acmicpc.net/problem/16928 뱀과 사다리 게임 <Silver I>"

num_of_ladder, num_of_snake = map(int, stdin.readline().split())

ladder = {}
snakes = {}

def read_targets(num_of_target):
    targets = {}
    for _ in range(num_of_target):
        start, to = map(int, stdin.readline().split())
        targets[start] = to

    return targets

ladder = read_targets(num_of_ladder)
snakes = read_targets(num_of_snake)

queue = deque([[1, 0]])
visited = {}
while queue:
    current, dice = queue.pop()

    if current == 100:
        print(dice)
        break

    find_snake = snakes.get(current)
    if find_snake:
        current = find_snake

    find_ladder = ladder.get(current)
    if find_ladder:
        current = find_ladder

    if visited.get(current):
        continue

    visited[current] = True

    new_dice = dice + 1
    for i in range(1, 7):
        new_target = current + i
        if new_target > 100:
            break

        queue.appendleft([new_target, new_dice])

