from sys import stdin
from collections import deque

"https://www.acmicpc.net/problem/9019 DSLR <Gold V>"

def register_shift_left(integer):
    return (integer % 1000) * 10 + integer // 1000

def register_shift_right(integer):
    return integer // 10 + integer % 10 * 1000

def search_command(origin, target):
    queue = deque()
    visited = [False for _ in range(10000)]

    queue.append((origin, ''))
    visited[origin] = True

    while queue:
        number, command = queue.popleft()
        if number == target:
            return command
 
        left = register_shift_left(number)
        right = register_shift_right(number)
        left_command = command + 'L'
        right_command = command + 'R'

        new_commands = [
            (number * 2 % 10000, command + "D"),
            (number - 1 if number != 0 else 9999, command + "S"),
            (left, left_command),
            (right, right_command)]


        for c in new_commands:
            if not visited[c[0]]:
                queue.append(c)
                visited[c[0]] = True

for i in range(int(stdin.readline())):
    origin, target = map(int, stdin.readline().split())
    print(search_command(origin, target))
