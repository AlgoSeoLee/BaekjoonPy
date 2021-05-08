from sys import stdin
from collections import deque

"https://www.acmicpc.net/problem/9019 DSLR <Gold V>"

def integer_to_array(number):
    array = []
    for i in range(4):
        array.append((number // (10 ** (3 - i))) % 10)
    return array

def array_to_integer(array):
    integer = 0
    for i in range(4):
        integer += array[i] * (10 ** (3 - i))
    return integer 

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
                left = arr 
                right = left.copy()
                left_command = command
                right_command = command
                for _ in range(2):
                    left = left[1:4] + [left[0]]
                    right = [right[3]] + right[0:3]
                    left_command += 'L'
                    right_command += 'R'
                    new_commands.append(
                        (array_to_integer(left), left_command))
                    new_commands.append(
                        (array_to_integer(right), right_command))
    
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
