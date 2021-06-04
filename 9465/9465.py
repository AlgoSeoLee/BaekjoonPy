from sys import stdin

"https://www.acmicpc.net/problem/9465 스티커 <Silver II>"

num_of_case = int(stdin.readline())
for _ in range(num_of_case):
    num_of_sticker_in_line = int(stdin.readline())

    stickers = [
        list(map(int, stdin.readline().split()))
        for _ in range(2)
    ]

    dp = [
        [0 for _ in range(3)]
        for _ in range(num_of_sticker_in_line + 1)
    ]

    for i in range(1, num_of_sticker_in_line + 1):
        prev = dp[i - 1]
        # 이번 줄에서 아무것도 선택하지 않을때
        dp[i][0] = max(prev)
        # 1번줄에서 스티커를 제거할떄
        dp[i][1] = max(prev[0],prev[2]) + stickers[0][i - 1]
        # 2번줄에서 스티커를 제거할떄
        dp[i][2] = max(prev[0],prev[1]) + stickers[1][i - 1]

    print(max(dp[num_of_sticker_in_line]))

