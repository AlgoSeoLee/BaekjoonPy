from sys import stdin

"https://www.acmicpc.net/problem/10866 덱 <실버 4>"

N = int(stdin.readline())
deque = []
for _ in range(N):
    line = stdin.readline().split()

    inst = line[0]
    var = None
    if len(line[1:]) == 1:
        var = line[1]

    if inst == "push_front":
        newDeque = [var]
        newDeque.extend(deque)
        deque = newDeque
    elif inst == "push_back":
        deque.append(var)
    elif inst == "pop_front":
        result = -1
        if len(deque) != 0:
            result = deque[0]
            deque = deque[1:]
        print(result)
    elif inst == "pop_back":
        result = -1
        if len(deque) != 0:
            result = deque.pop()
        print(result)
    elif inst == "size":
        print(len(deque))
    elif inst == "empty":
        out = 0
        if len(deque) == 0:
            out = 1
        print(out)
    elif inst == "front":
        result = -1
        if len(deque) != 0:
            result = deque[0]
        print(result)
    elif inst == "back":
        result = -1
        if len(deque) != 0:
            result = deque[-1]
        print(result)
