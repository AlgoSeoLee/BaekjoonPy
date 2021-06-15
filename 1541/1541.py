from sys import stdin
from collections import deque
import re

"https://www.acmicpc.net/problem/1541 잃어버린 괄호 <Silver II>"

REGEXP = re.compile(r"[+-]")
def solve_minimize(plain):
    operators = REGEXP.findall(plain)
    numbers = deque(map(int,REGEXP.split(plain)))

    length_of_operators = len(operators)
    current = 0
    total = numbers.popleft()
    while current < length_of_operators:
        current_op = operators[current]
        current_num = numbers.popleft()

        if current_op == '-':
            try:
                while True:
                    next_op = operators[current+1]
                    if next_op == '+':
                        current += 1
                        current_num += numbers.popleft()
                    else:
                        break
            except IndexError:
                pass

            total -= current_num
        elif current_op == '+':
            total += current_num

        current += 1

    return total

print(solve_minimize(stdin.readline()))
