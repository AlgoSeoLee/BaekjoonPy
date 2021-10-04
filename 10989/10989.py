from sys import stdin

"https://www.acmicpc.net/problem/10989 수 정렬하기 3 <Silver V>"

length = int(stdin.readline())
existence = {}

for _ in range(length):
    target = int(stdin.readline())
    duplicate = existence.get(target)
    if not duplicate:
        duplicate = 0
    duplicate += 1
    existence[target] = duplicate

for target in range(1, 10001):
    duplicate = existence.get(target)
    if duplicate:
        for _ in range(duplicate):
            print(target)

