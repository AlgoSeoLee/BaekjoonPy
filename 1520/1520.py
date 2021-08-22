from sys import stdin
from collections import deque

read_integers = lambda: map(int, stdin.readline().split())

def input_matrix(num_of_row):
    return [
        [v for v in read_integers()]
        for _ in range(num_of_row)
    ]

DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

def solve_find_downhill_ways(num_of_row, num_of_column, matrix):
    queue = deque()
    visited = {}

    start_height = matrix[0][0]
    queue.append((0, 0, start_height))

    result = 0
    endpoint = (
        num_of_column - 1,
        num_of_row - 1
    )

    get_height = lambda w: matrix[w[1]][w[0]]

    while queue:
        current = queue.pop()
        x, y, total = current

        ways = map(lambda d: (x + d[0], y + d[1]), DIRECTIONS)
        ways = filter(lambda w: w[0] >= 0 and w[0] < num_of_column, ways)
        ways = filter(lambda w: w[1] >= 0 and w[1] < num_of_row, ways)
        ways = list(map(
            lambda w: (w[0], w[1], total + get_height(w)),
            ways
        ))
        ways = filter(lambda w: not visited.get(w), ways)
        ways = filter(lambda w: get_height(w) < get_height(current), ways)

        for w in ways:
            if w[:2] == endpoint:
                result += 1
            else:
                queue.appendleft(w)
                visited[w] = True

    return result

num_of_row, num_of_column = read_integers()
matrix = input_matrix(num_of_row)
print(solve_find_downhill_ways(num_of_row, num_of_column, matrix))

