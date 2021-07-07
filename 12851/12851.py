from sys import stdin
from collections import deque

def BFS(start, target):
    visited = {}
    visited[start] = True
    queue = deque()
    queue.appendleft((start, 0))
    startFromOne = start == 1

    result = []
    while queue:
        current, level = queue.pop()
        if current == target:
            result.append(level)
            continue

        ways = []
        plus = current + 1
        minus = current - 1
        double = current * 2

        if startFromOne and plus == double:
            dup = True
            ways.append(plus)
        else:
            ways.append(plus)
            ways.append(double)

        ways.append(minus)
        ways = filter(lambda w: w >= 0 and w <= 100000, ways)

        next_level = level + 1
        for n in ways:
            if not visited.get(n):
                if n != target:
                    visited[n] = True
                queue.appendleft((n, next_level))

    if startFromOne:
        result.extend(result)

    return result

subin, brother = map(int, stdin.readline().split())
result = BFS(subin, brother)
print(min(result))
print(len(result))

