from sys import stdin

"https://www.acmicpc.net/problem/1932 정수 삼각형 <Silver I>"

num_of_line = int(stdin.readline())
triangle = [
    [int(v) for v in stdin.readline().split()]
    for _ in range(num_of_line)
]

dp = [triangle[0]]
dp.extend([[] for _ in range(1, num_of_line)])

for current in range(1, num_of_line):
    line = triangle[current]
    result = dp[current]
    prev = dp[current - 1]

    result.append(prev[0] + line[0])
    for pos in range(1, current):
        result.append(max(prev[pos - 1:pos + 1]) + line[pos])
    result.append(prev[current - 1] + line[current])

print(max(dp[num_of_line - 1]))
