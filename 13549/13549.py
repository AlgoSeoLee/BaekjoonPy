from sys import stdin
from collections import deque

"https://www.acmicpc.net/problem/13549 숨바꼭질 3 <Gold V>"

MAXIMUM = 100000
MINIMUM = 0

def finding_shortest_time(start, target):
    queue = deque()
    queue.append((0, start))
    visited = [False for _ in range(MAXIMUM + 1)]

    while queue:
        current_cost, current = queue.popleft()

        if current == target:
            return current_cost

        double = current * 2
        minus = current - 1
        plus = current + 1

        if double > MINIMUM and double <= MAXIMUM and not visited[double]:
            visited[double] = True
            queue.appendleft((current_cost, double))
        if plus <= MAXIMUM and not visited[plus]:
            visited[plus] = True
            queue.append((current_cost + 1, plus))
        if minus >= MINIMUM and not visited[minus]:
            visited[minus] = True
            queue.append((current_cost + 1, minus))

start, target = map(int, stdin.readline().split())
print(finding_shortest_time(start, target))
