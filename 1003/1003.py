from sys import stdin

dp = [[1, 0], [0, 1]]
start = 2

def calc_num_of_printed_01(target):
    global dp
    global start

    end = target + 1
    for i in range(start, end):
        dp[0].append(dp[0][i - 2] + dp[0][i - 1])
        dp[1].append(dp[1][i - 2] + dp[1][i - 1])

    if start < end:
        start = end
    return (dp[0][target], dp[1][target])

num_of_case = int(stdin.readline())
for _ in range(num_of_case):
    target = int(stdin.readline())
    for i in calc_num_of_printed_01(target):
        print(i, end=" ")
    print()

