from sys import stdin

def longest_common_subsequence(plain_A, plain_B):
    length_of_A = len(plain_A) + 1
    length_of_B = len(plain_B) + 1

    dp = []
    for y in range(length_of_B):
        dp.append([])
        for x in range(length_of_A):
            add = 0
            if y == 0 or x == 0:
                pass
            elif plain_A[x - 1] == plain_B[y - 1]:
                add = dp[y - 1][x - 1] + 1
            else:
                add = max(dp[y][x - 1], dp[y - 1][x])

            dp[y].append(add)

    subsequence = ''
    x = length_of_A - 1
    y = length_of_B - 1
    while dp[y][x] != 0:
        current_score = dp[y][x]
        if dp[y - 1][x] == current_score:
            y -= 1
        elif dp[y][x - 1] == current_score:
            x -= 1
        else:
            subsequence = plain_A[x - 1] + subsequence
            x -= 1
            y -= 1

    return subsequence

plain_A = stdin.readline().rstrip()
plain_B = stdin.readline().rstrip()

print(len(longest_common_subsequence(plain_A, plain_B)))

