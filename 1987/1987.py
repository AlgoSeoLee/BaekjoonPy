from sys import stdin, maxsize

def input_board(num_of_row):
    return [
        stdin.readline().rstrip()
        for _ in range(num_of_row)
    ]

def solve_alphabet(board, num_of_row, num_of_column):
    stack = []
    visited = [
        [-1 for _ in range(num_of_column)]
        for _ in range(num_of_row)
    ]

    DIRECTION = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ]

    result = -1
    stack.append((0, 0, set(board[0][0])))
    visited[0][0] = 0
    while stack:
        x, y, path = stack.pop()
        level = len(path) + 1

        ways = map(lambda d: (x + d[0], y + d[1]), DIRECTION)
        ways = filter(
            lambda w:
                w[0] >= 0 and w[0] < num_of_column and
                w[1] >= 0 and w[1] < num_of_row,
            ways
        )
        ways = filter(lambda w: not board[w[1]][w[0]] in path, ways)
        ways = map(
            lambda w: (w[0], w[1], path.union(board[w[1]][w[0]])),
            ways
        )
        ways = filter(lambda w: level >= visited[w[1]][w[0]], ways)

        for w in ways:
            if level >= result:
                result = level
            stack.append(w)
            visited[w[1]][w[0]] = level

    return result

num_of_row, num_of_column = map(int, stdin.readline().split())
board = input_board(num_of_row)

print(solve_alphabet(board, num_of_row, num_of_column))
