from sys import stdin
from itertools import accumulate

"https://www.acmicpc.net/problem/11660 구간 합 구하기 5 <Silver I>"

matrix_size, num_of_answer = map(int, stdin.readline().split())
matrix = [
    [int(elem) for elem in stdin.readline().split()]
    for _ in range(matrix_size)
]
matrix_prefix = [
    list(accumulate(line, lambda a, x: a + x))
    for line in matrix
]

for _ in range(num_of_answer):
    sy, sx, ey, ex = map(lambda x: int(x) - 1, stdin.readline().split())
    if sx == ex and sy == ey:
        print(matrix[sy][sx])
        continue

    result = 0
    before = sx - 1
    for iy in range(sy, ey + 1):
        start = 0
        if before >= 0:
            start = matrix_prefix[iy][before]
        end = matrix_prefix[iy][ex]
        result += end - start

    print(result)

