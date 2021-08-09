from sys import stdin, exit

num_of_wine = int(stdin.readline())

wines = []
for _ in range(num_of_wine):
    wines.append(int(stdin.readline()))

if num_of_wine <= 2:
    print(sum(wines))
    exit(0)

dp = [0, wines[0], wines[0] + wines[1]]
for i in range(3, num_of_wine + 1):
    dp.append(max(
        dp[i - 3] + wines[i - 2] + wines[i - 1],
        dp[i - 2] + wines[i - 1],
        dp[i - 1]
    ))

print(dp[-1])

