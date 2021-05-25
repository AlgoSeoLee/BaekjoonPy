from sys import stdin
from collections import deque
from enum import Enum
from functools import reduce

RGB = Enum("RGB", "Red Green Blue RedGreen")

def dispense_RGB(c):
    if c == "R":
        return RGB.Red
    elif c == "G":
        return RGB.Green
    elif c == "B":
        return RGB.Blue

def _BFS(
    matrix, target_RGB, is_weakness,
    total_x, total_y, start_x, start_y, visited):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_y][start_x] = True

    while queue:
        x, y = queue.popleft()

        diff = []
        if x != 0:
            diff.append((-1, 0))
        if x != total_x - 1:
            diff.append((1, 0))
        if y != 0:
            diff.append((0, -1))
        if y != total_y - 1:
            diff.append((0, 1))

        for d in diff:
            dx = x + d[0]
            dy = y + d[1]
            is_visited = not visited[dy][dx]

            current = matrix[dy][dx]
            is_current_RedGreen = current == RGB.Green or current == RGB.Red
            is_target_RedGreen = target_RGB == RGB.Green or target_RGB == RGB.Red
            if target_RGB == RGB.RedGreen:
                if is_current_RedGreen:
                    current = RGB.RedGreen
            is_target = current == target_RGB
            if not is_target and is_target_RedGreen and is_weakness:
                if is_current_RedGreen:
                    target_RGB = RGB.RedGreen
                    is_target = True

            if is_visited and is_target:
                visited[dy][dx] = True
                queue.append((dx, dy))

    return target_RGB

def calc_num_of_area(matrix, total_x, total_y, is_weakness):
    visited = [[False for _ in range(total_x)] for _ in range(total_y)]
    get_target_RGB = lambda x,y: matrix[y][x]

    result = {
        RGB.Red: 0,
        RGB.Green: 0,
        RGB.Blue: 0,
        RGB.RedGreen: 0
    }
    for start_y in range(total_y):
        for start_x in range(total_x):
            is_visited = not visited[start_y][start_x]
            target_RGB = get_target_RGB(start_x,start_y)
            if is_visited:
                target_RGB = _BFS(matrix, target_RGB, is_weakness,
                    total_x, total_y, start_x, start_y, visited)
                result[target_RGB] += 1

    return result


size = int(stdin.readline())
matrix = [
    list(map(dispense_RGB, stdin.readline().rstrip()))
    for _ in range(size)
]

RGB_area = calc_num_of_area(matrix, size, size, False)
RG_weak_area = calc_num_of_area(matrix, size, size, True)
num_of_RGB_area = reduce(lambda acc, rgb: acc + RGB_area[rgb], RGB_area, 0)
num_of_RG_weak_area = reduce(lambda acc, rgb: acc + RG_weak_area[rgb], RG_weak_area, 0)
print("{} {}".format(num_of_RGB_area,num_of_RG_weak_area))

