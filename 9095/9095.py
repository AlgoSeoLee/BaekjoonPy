from sys import stdin

"https://www.acmicpc.net/problem/9095 1, 2, 3 더하기 <Silver III>"

dp = [1, 2, 4]

case = int(stdin.readline())

for _ in range(case):
    target = int(stdin.readline())
    if len(dp) == target:
        print(dp[target-1])
        continue

    for cur in range(len(dp), target):
        dp.append(dp[cur-3] + dp[cur-2] + dp[cur-1])

    print(dp[target-1])
