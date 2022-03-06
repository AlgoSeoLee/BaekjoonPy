from sys import stdin

"https://www.acmicpc.net/problem/9461 파도반 수열 <Silver III>"

dp = [1, 1, 1]

def calc_numbers_of_triangle(target):
    start = len(dp)
    if start < target:
        for i in range(start, target):
            dp.append(dp[i - 2] + dp[i - 3])

    return dp[target - 1]

for _ in range(int(stdin.readline())):
    print(calc_numbers_of_triangle(int(stdin.readline())))
