from sys import stdin
from collections import deque

belt_len, belt_limit = map(int, stdin.readline().split())
belt_life = deque([int(v) for v in stdin.readline().split()])
belt_robot = deque([False for _ in range(belt_len)])

loop = 1

while True:
    belt_life.appendleft(belt_life.pop())
    belt_robot.pop()
    belt_robot.appendleft(False)

    belt_robot[-1] = False

    for idx in range(belt_len - 2, 0, -1):
        if belt_robot[idx] and not belt_robot[idx+1] and belt_life[idx+1]:
            print(idx)
            belt_robot[idx] = False
            belt_robot[idx+1] = True
            belt_life[idx+1] -= 1

    if belt_life[0] and not belt_robot[0]:
        belt_life[0] -= 1
        belt_robot[0] = True

    count = 0
    for life in belt_life:
        if life == 0:
            count += 1

    if count >= belt_limit:
        break

    loop += 1

print(loop)
