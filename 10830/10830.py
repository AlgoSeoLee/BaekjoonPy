from sys import stdin

"https://www.acmicpc.net/problem/10830 행렬 제곱 <Gold IV>"

MOD = 1000
def matrix_mul(size, a, b):
    c = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= MOD

    return c

size, times = map(int, stdin.readline().split())
matrix = [[int(v) for v in stdin.readline().split()] for _ in range(size)]
result = [[v % 1000 for v in line] for line in matrix]
times -= 1

while times > 0:
    if times % 2 == 1:
        result = matrix_mul(size, result, matrix)

    matrix = matrix_mul(size, matrix, matrix)
    times //= 2

for i in range(size):
    for j in range(size):
        print(result[i][j], end=' ')
    print()

