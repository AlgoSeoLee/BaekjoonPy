from sys import stdin

"https://www.acmicpc.net/problem/11727 2×n 타일링 2 <Silver III>"

x_length = int(stdin.readline())
x_length += 1

y = [0 for _ in range(x_length)]
y[0] = 1
y[1] = 1

for i in range(2, x_length):
    y[i] = y[i - 1] + 2 * y[i - 2]

print(y[x_length - 1] % 10007)

