from sys import stdin
from math import log
from collections import deque

TRIFORCE = [
    "  *  ",
    " * * ",
    "*****"
]

def blank(x, y):
    result = []
    for i in range(y):
        result.append('')
        for j in range(x):
            result[i] += ' '

    return result

def make_triforce_pyramid(num_of_line):
    level = int(log(num_of_line / 3, 2))
    if level == 0:
        return deque(TRIFORCE)

    prev_lines = (2 ** (level - 1)) * 3
    triforce = make_triforce_pyramid(prev_lines)
    tmp_triforce = triforce.copy()

    for i in range(prev_lines):
        triforce[i] = triforce[i] + ' ' + triforce[i]

    for i in range(prev_lines):
        tmp_blank = prev_lines * ' '
        tmp_triforce[i] = tmp_blank + tmp_triforce[i] + tmp_blank

    tmp_triforce.extend(triforce)

    return tmp_triforce

num_of_line = int(stdin.readline())
for line in make_triforce_pyramid(num_of_line):
    print(line)
