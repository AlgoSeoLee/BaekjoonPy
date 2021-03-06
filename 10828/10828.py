from sys import stdin

"https://www.acmicpc.net/problem/10828 스택 <실버 4>"

N = int(stdin.readline())
stack = []
for _ in range(N):
    line = stdin.readline().split()

    inst = line[0]
    var = None
    if len(line[1:]) == 1:
        var = line[1]

    if inst == "push":
        stack.append(var)
    elif inst == "pop":
        result = -1
        if len(stack) != 0:
            result = stack.pop()
        print(result)
    elif inst == "size":
        print(len(stack))
    elif inst == "empty":
        out = 0
        if len(stack) == 0:
            out = 1
        print(out)
    elif inst == "top":
        result = -1
        if len(stack) != 0:
            result = stack[-1]
        print(result)
