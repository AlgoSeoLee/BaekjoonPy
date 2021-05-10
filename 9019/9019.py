from sys import stdin
from collections import deque

"https://www.acmicpc.net/problem/9019 DSLR <Gold V>"

def integer_to_array(number):
    array = []
    for i in range(4):
        array.append((number // (10 ** (3 - i))) % 10)
    return array

def register_shift_left(integer):
    return (integer % 1000) * 10 + integer // 1000

def register_shift_right(integer):
    return integer // 10 + integer % 10 * 1000

def search_command(origin, target):
    queue = deque()
    visited = dict()

    queue.append((origin, ''))
    visited[origin] = ''

    try:
        while True:
            number, command = queue.popleft()
            if number == target:
                return command
    
            new_commands = [
                (number * 2 % 10000, command + "D"),
                (number - 1 if number != 0 else 9999, command + "S")]
    
            shift_commands = ""
            priv_command = command[-1] if len(command) != 0 else ''
            arr = integer_to_array(number)
            elem = set(arr)
            if len(elem) != 1 and priv_command != 'L' and priv_command != 'R':
                left = number
                right = number
                left_command = command
                right_command = command
                for _ in range(2):
                    left = register_shift_left(left)
                    right = register_shift_right(right)
                    left_command += 'L'
                    right_command += 'R'
                    new_commands.append(
                        (left, left_command))
                    new_commands.append(
                        (right, right_command))
    
            for c in new_commands:
                if c[0] == target:
                    return c[1]
    
                if visited.get(c[0]) == None:
                    queue.append(c)
                    visited[c[0]] = c[1]

    except IndexError:
        pass

for i in range(int(stdin.readline())):
    origin, target = map(int, stdin.readline().split())
    print(search_command(origin, target))
