from sys import stdin
from itertools import chain, combinations

"https://www.acmicpc.net/problem/15686 치킨 배달 <Gold V>"

size, num_of_survivor = map(int, stdin.readline().split())

houses = []
stores = []
for x in range(size):
    for y, v in zip(range(size), stdin.readline().split()):
        current = (x, y)
        if v == '1':
            houses.append(current)
        elif v == '2':
            stores.append(current)

comb = combinations(stores, 1)
for i in range(2, num_of_survivor + 1):
    comb = chain(
        combinations(stores, i),
        comb
    )

result = []
for c in comb:
    distance = 0
    for h in houses:
        distance += min(
            map(lambda s: abs(h[0] - s[0]) + abs(h[1] - s[1]), c)
        )
    result.append(distance)

print(min(result))
