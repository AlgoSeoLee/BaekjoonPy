from sys import stdin

"https://www.acmicpc.net/problem/2096 내려가기 <Gold IV>"

num_of_line = int(stdin.readline())

min_dp = [int(v) for v in stdin.readline().split()]
max_dp = min_dp.copy()

def calc_dp(func, dp, prev, line):
    dp[0] = line[0] + func(prev[0:2])
    dp[1] = line[1] + func(prev[0:3])
    dp[2] = line[2] + func(prev[1:3])

for _ in range(1, num_of_line):
    line = [int(v) for v in stdin.readline().split()]
    min_prev = min_dp.copy()
    max_prev = max_dp.copy()
    calc_dp(max, max_dp, max_prev, line)
    calc_dp(min, min_dp, min_prev, line)

print(max(max_dp), min(min_dp))
