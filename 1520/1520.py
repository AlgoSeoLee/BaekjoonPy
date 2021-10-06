from sys import stdin, setrecursionlimit

"https://www.acmicpc.net/problem/1520 내리막 길 <Gold IV>"

setrecursionlimit(10 ** 4)
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

def _DFS(matrix, visited, num_of_row, num_of_column, row, column):
    get_height = lambda r, c: matrix[r][c]
    is_visited = lambda r, c: visited[r][c]

    if (row == num_of_row - 1 and column == num_of_column - 1):
        return 1

    target_way = is_visited(row, column)
    if target_way != 0:
        return target_way

    height_when_entered = get_height(row, column)

    ways = map(
        lambda d: (row + d[0], column + d[1]),
        DIRECTIONS
    )
    ways = filter(
        lambda w:
            w[0] >= 0 and w[0] < num_of_row and
            w[1] >= 0 and w[1] < num_of_column and
            is_visited(w[0], w[1]) != -1,
        ways
    )
    ways = list(map(lambda w: (get_height(w[0], w[1]), w[0], w[1]), ways))
    ways.sort()

    visited[row][column] = -1
    acc = 0
    for h, r, c in ways:
        if h < height_when_entered:
            acc += _DFS(matrix, visited, num_of_row, num_of_column, r, c)
        else:
            break

    if acc != 0:
        visited[row][column] = acc
    else:
        visited[row][column] = -1

    return acc

def solve_find_downhill_ways(num_of_row, num_of_column, matrix):
    visited = [
        [0 for _ in range(num_of_column)]
        for _ in range(num_of_row)
    ]
    result = _DFS(matrix, visited, num_of_row, num_of_column, 0, 0)
    return result

num_of_row, num_of_column = read_integers()
matrix = input_matrix(num_of_row)
print(solve_find_downhill_ways(num_of_row, num_of_column, matrix))

