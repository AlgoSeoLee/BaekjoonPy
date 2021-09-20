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

def calcAlphabetIdx(char):
    return ord(char) - 65

def _dfs(board, num_of_row, num_of_column, row, column, level, visited):
    alphabetIndex = calcAlphabetIdx(board[row][column])
    visited[alphabetIndex] = True

    result = level
    for d in DIRECTION:
        way = (column + d[0], row + d[1])
        cond = (
            way[0] >= 0 and way[0] < num_of_column and
            way[1] >= 0 and way[1] < num_of_row and
            not visited[calcAlphabetIdx(board[way[1]][way[0]])]
        )
        if cond:
            explore = _dfs(
                board, num_of_row, num_of_column,
                way[1], way[0], level + 1, visited
            )
            result = explore if explore > result else result
    
    visited[alphabetIndex] = False

    return result

def solve_alphabet(board, num_of_row, num_of_column):
    visited = [False for _ in range(26)]

    return _dfs(board, num_of_row, num_of_column, 0, 0, 1, visited)

num_of_row, num_of_column = map(int, stdin.readline().split())
board = input_board(num_of_row)

print(solve_alphabet(board, num_of_row, num_of_column))
