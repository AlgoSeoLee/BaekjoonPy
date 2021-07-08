from sys import stdin
from collections import deque

"https://www.acmicpc.net/problem/12851 숨바꼭질 2 <Gold V>"

def BFS(start, target):
    queue = deque()
    queue.appendleft((start, 0))
    visited = {}
    visited[start] = 1

    min_level = 100000
    method = 0

    ops = [
        lambda a: a + 1,
        lambda a: a - 1,
        lambda a: a * 2
    ]

    while queue:
        current, level = queue.pop()
        if current == target:
            if level == min_level:
                method += 1
            elif level < min_level:
                min_level = level
                method = 1
            continue

        ways = map(lambda f: f(current), ops)
        ways = filter(lambda w: w >= 0 and w <= 100000, ways)

        next_level = level + 1
        for n in ways:
            if not visited.get(n) or visited[n] >= next_level:
                if n != target:
                    visited[n] = next_level
                queue.appendleft((n, next_level))

    return min_level, method

subin, brother = map(int, stdin.readline().split())
level, method = BFS(subin, brother)
print(level)
print(method)
