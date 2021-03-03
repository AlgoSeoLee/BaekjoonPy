from sys import stdin

"https://www.acmicpc.net/problem/1654 랜선 자르기 <실버 3>"

N, target = map(int, stdin.readline().rstrip().split())

lines = []
for _ in range(N):
    lines.append(int(stdin.readline()))

start = 1
end = max(lines)
length = 0
while start <= end:
    current = (start + end) // 2

    cut = 0
    for l in lines:
        cut = cut + l // current

    if cut >= target:
        if current > length:
            length = current

        start = current + 1
    else:
        end = current - 1

print(length)
