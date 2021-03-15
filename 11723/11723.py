from sys import stdin

"https://www.acmicpc.net/problem/11723 집합 <Silver V>"

EMPTY = 0b00000000000000000000
ALL = 0b11111111111111111111

problem = EMPTY

operations = int(stdin.readline())
for _ in range(operations):
    ops = stdin.readline().rstrip()

    empty_or_all = None
    if ops == "empty":
        empty_or_all = EMPTY
    elif ops == "all":
        empty_or_all = ALL

    if empty_or_all is not None:
        problem = empty_or_all
        continue

    ops, target = ops.split()
    target = int(target) - 1

    if ops == "add":
        problem = problem | (1 << target)
    elif ops == "remove":
        problem = problem & ~(1 << target)
    elif ops == "check":
        state = 0
        if problem & (1 << target) != 0:
            state = 1

        print(state)
    elif ops == "toggle":
        problem = problem ^ (1 << target)
