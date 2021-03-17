from sys import stdin

OUT = 10**6 + 1

dp = [0, 1, 1]
target = int(stdin.readline())

for cur in range(4, target+1):
    selection = [OUT, OUT, dp[cur - 2]]
    if cur % 3 == 0:
        selection[0] = dp[cur // 3 - 1]
    if cur % 2 == 0:
        selection[1] = dp[cur // 2 - 1]

    solve = min(selection) + 1
    dp.append(solve)

print(dp[target-1])
