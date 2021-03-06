from sys import stdin

"https://www.acmicpc.net/problem/10845 큐 <실버 4>"

N = int(stdin.readline())
queue = []
for _ in range(N):
    line = stdin.readline().split()

    inst = line[0]
    var = None
    if len(line[1:]) == 1:
        var = line[1]

    if inst == "push":
        newQueue = [var]
        newQueue.extend(queue)
        queue = newQueue
    elif inst == "pop":
        result = -1
        if len(queue) != 0:
            result = queue.pop()
        print(result)
    elif inst == "size":
        print(len(queue))
    elif inst == "empty":
        out = 0
        if len(queue) == 0:
            out = 1
        print(out)
    elif inst == "front":
        result = -1
        if len(queue) != 0:
            result = queue[-1]
        print(result)
    elif inst == "back":
        result = -1
        if len(queue) != 0:
            result = queue[0]
        print(result)
