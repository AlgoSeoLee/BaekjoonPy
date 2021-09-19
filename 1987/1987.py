from sys import stdin, maxsize

"https://www.acmicpc.net/problem/1987 알파벳 <Gold IV>"

def input_board(num_of_row):
    return [
        stdin.readline().rstrip()
        for _ in range(num_of_row)
    ]

DIRECTION = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

def _dfs(board, num_of_row, num_of_column, row, column, level, visited):
    level += 1
    alphabetIndex = ord(board[row][column]) - 65
    if visited[alphabetIndex]:
        return level - 1

    ways = map(lambda d: (d[0] + column, d[1] + row), DIRECTION)
    ways = filter(
        lambda w:
            w[0] >= 0 and w[0] < num_of_column and
            w[1] >= 0 and w[1] < num_of_row,
        ways
    )

    visited[alphabetIndex] = True

    result = max(
        map(
            lambda w: _dfs(
                board, num_of_row, num_of_column,
                w[1], w[0], level, visited
            ),
            ways
        )
    )

    visited[alphabetIndex] = False

    return result

def solve_alphabet(board, num_of_row, num_of_column):
    visited = [False for _ in range(26)]

    return _dfs(board, num_of_row, num_of_column, 0, 0, 0, visited)

num_of_row, num_of_column = map(int, stdin.readline().split())
board = input_board(num_of_row)

print(solve_alphabet(board, num_of_row, num_of_column))
