from sys import stdin
from heapq import heappop, heappush

"https://www.acmicpc.net/problem/13549 숨바꼭질 3 <Gold V>"

MAXIMUM = 100000
MINIMUM = 0

def finding_shortest_time(start, target):
    queue = []
    queue.append((0, start))
    visited = [False for _ in range(MAXIMUM + 1)]

    while queue:
        current_cost, current = heappop(queue)

        if current == target:
            return current_cost

        double = current * 2
        minus = current - 1
        plus = current + 1

        ways = []
        if double > MINIMUM and double <= MAXIMUM :
            ways.append((current_cost, double))
        if plus >= MINIMUM and plus <= MAXIMUM:
            ways.append((current_cost + 1, plus))
        if minus >= MINIMUM and minus <= MAXIMUM:
            ways.append((current_cost + 1, minus))

        for w in ways:
            if not visited[w[1]]:
                visited[w[1]] = True
                heappush(queue, w)

start, target = map(int, stdin.readline().split())
print(finding_shortest_time(start, target))
