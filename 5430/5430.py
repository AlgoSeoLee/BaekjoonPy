from sys import stdin
from collections import deque

num_of_test = int(stdin.readline())

for _ in range(num_of_test):
    commands = stdin.readline().rstrip()
    stdin.readline()
    plain = stdin.readline()[1:-2]
    arr = deque()
    if len(plain) != 0:
        arr.extend(map(int, plain.split(',')))

    is_error = False
    is_reverse = False
    for c in commands:
        if c == 'R':
            is_reverse = not is_reverse
        elif c == 'D':
            try:
                if not is_reverse:
                    arr.popleft()
                else:
                    arr.pop()
            except IndexError:
                is_error = True
                break

    if is_error:
        print('error')
    else:
        if is_reverse:
            arr = reversed(arr)

        print('[', end='')
        start = True
        for num in arr:
            if not start:
                print(',', end='')
            print(num, end='')
            start = False
        print(']')

