from sys import stdin
from queue import Queue

"https://www.acmicpc.net/problem/9019 DSLR <Gold V>"

def integer_to_digit(number):
    register = str(number)
    return "0" * (4 - len(register)) + register

def search_command(origin, target):
    queue = Queue()

    queue.put((origin, ''))

    while not queue.empty():
        number, command = queue.get()
        if number == target:
            return command

        new_commands = [
            (number * 2 % 10000, command + "D"),
            (number - 1 if number != 0 else 9999, command + "S")]

        shift_commands = ""
        priv_command = command[-1] if len(command) != 0 else ''
        if priv_command != 'L' and priv_command != 'R':
            left = integer_to_digit(number)
            right = left
            left_command = command
            right_command = command
            for _ in range(3):
                left = left[1:4] + left[0]
                right = right[3] + right[0:3]
                left_command += 'L'
                right_command += 'R'
                new_commands.append((int(left), left_command))
                new_commands.append((int(right), right_command))

        for c in new_commands:
            if c[0] == target:
                return c[1]
            queue.put(c)

for i in range(int(stdin.readline())):
    origin, target = map(int, stdin.readline().split())
    print(search_command(origin, target))
