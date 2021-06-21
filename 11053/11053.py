from sys import stdin

"https://www.acmicpc.net/problem/11053 가장 긴 증가하는 부분 수열 <Silver II>"

length_of_sequence = int(stdin.readline()) + 1
sequence = list(map(int, stdin.readline().split()))
element = sorted(set(sequence))
length_of_element = len(element) + 1

dp = [
    [0 for _ in range(length_of_sequence)]
    for _ in range(length_of_element)
]

for i in range(1, length_of_element):
    current_elem = element[i - 1]
    for j in range(1, length_of_sequence):
        current_num = sequence[j - 1]
        if current_num == current_elem:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[length_of_element - 1][length_of_sequence - 1])

