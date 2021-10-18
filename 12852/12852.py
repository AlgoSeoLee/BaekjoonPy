from sys import stdin, maxsize

"https://www.acmicpc.net/problem/12852 1로 만들기 2 <Silver I>"

def solve_to_1(target):
    dp = [0, 1, 1]
    for cur in range(4, target + 1):
        selection = []
        if cur % 2 == 0:
            selection.append(dp[cur // 2 - 1])
        if cur % 3 == 0:
            selection.append(dp[cur // 3 - 1])
        selection.append(dp[cur - 2])

        dp.append(min(selection) + 1)

    backtrack = [target]
    cur = target
    while cur != 1:
        selection = cur - 1
        selection_length = dp[cur - 2]

        if cur % 3 == 0:
            div_by_3 = dp[cur // 3 - 1]
            if div_by_3 < selection_length:
                selection = cur // 3
                selection_length = div_by_3

        if cur % 2 == 0:
            div_by_2 = dp[cur // 2 - 1]
            if div_by_2 < selection_length:
                selection = cur // 2
                selection_length = div_by_2

        backtrack.append(selection)
        cur = selection

    return dp[target - 1], backtrack

target = int(stdin.readline())
ops, backtrack = solve_to_1(target)
print(ops)
print(*backtrack)
