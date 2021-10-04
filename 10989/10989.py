from sys import stdin

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

