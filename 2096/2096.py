from sys import stdin

"https://www.acmicpc.net/problem/2096 내려가기 <Gold IV>"

def init_dp(matrix, matrix_size):
    dp = [
        [0 for _ in range(matrix_size)]
        for _ in range(matrix_size)
    ]
    for i in range(matrix_size):
        dp[0][i] = matrix[0][i]

    return dp

def calc_both(matrix_line, func, last, cur_line, prev_line, dp):
    cur_line[0] = func(prev_line[0], prev_line[1])
    cur_line[0] += matrix_line[0]
    cur_line[last] = func(prev_line[last], prev_line[last-1])
    cur_line[last] += matrix_line[last]

def calc_dp(matrix_line, func, cur_line, prev_line, index, dp):
    value = matrix_line[index]
    value += func(
        prev_line[index - 1],
        prev_line[index],
        prev_line[index+1]
    )
    cur_line[index] = value

matrix_size = int(stdin.readline())
matrix = [
    list(map(int, stdin.readline().split()))
    for _ in range(matrix_size)
]
dp = init_dp(matrix, matrix_size)

def run_dp(func):
    last = matrix_size - 1
    for line_num in range(1, matrix_size):
        cur_line = dp[line_num]
        prev_line = dp[line_num - 1]
        matrix_line = matrix[line_num]

        calc_both(matrix_line, func, last, cur_line, prev_line, dp)

        for index in range(1, last):
            calc_dp(matrix_line, func, cur_line, prev_line, index, dp)

    return func(dp[last])

print(run_dp(max), run_dp(min))

