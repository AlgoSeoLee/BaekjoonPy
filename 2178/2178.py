from sys import stdin
from collections import deque

def solve_maze(matrix, total_x, total_y):
    visited = [[False for _ in range(total_x)] for _ in range(total_y)]
    queue = deque([(0, 0, 1)])
    visited[0][0] = True

    while queue:
        [x, y, times] = queue.popleft()
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1),
        ]
        positions = map(lambda d: (x + d[0], y + d[1]), directions)
        positions = filter(
            lambda d: d[0] < total_x and d[1] < total_y and d[0] >= 0 and d[1] >= 0,
            positions)
        positions = filter(
            lambda d: not visited[d[1]][d[0]] and matrix[d[1]][d[0]],
            positions)
        positions = map(lambda d: (d[0], d[1], times + 1), positions)
        positions = list(positions)
        queue.extend(positions)
        for dx, dy,t in positions:
            visited[dy][dx] = True
            if dx == total_x - 1 and dy == total_y - 1:
                return t

total_y, total_x = map(int, stdin.readline().split())

matrix = [
    list(map(lambda x: x == '1', stdin.readline()))
    for _ in range(total_y)]
print(solve_maze(matrix, total_x, total_y))
