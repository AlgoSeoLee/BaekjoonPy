from sys import stdin
from itertools import accumulate

"https://www.acmicpc.net/problem/11659 구간 합 구하기 4 <Silver III>"

_, num_of_answer = map(int, stdin.readline().split())
element = map(int, stdin.readline().split())
prefix = list(accumulate(element, lambda a, x: a + x))
for _ in range(num_of_answer):
    x, y = map(lambda x: int(x) - 1, stdin.readline().split())
    result = prefix[y]
    if x != 0:
        result -= prefix[x - 1]

    print(result)

