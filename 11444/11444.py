from sys import stdin

"https://www.acmicpc.net/problem/11444 피보나치 수 6 <Gold III>"

MOD = 1000000007

def matrix_mul(size, a, b):
    c = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= MOD

    return c

def fibo(times):
    if times <= 0:
        return 0
    elif times <= 2:
        return 1

    answer = [[1, 0], [0, 1]]
    acc = [[1, 1], [1, 0]]
    while times > 0:
        if times % 2 == 1:
            answer = matrix_mul(2, answer, acc)
        acc = matrix_mul(2, acc, acc)
        times //= 2

    return answer[0][1]

print(fibo(int(stdin.readline())))
