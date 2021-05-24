from sys import stdin
from collections import deque
from enum import Enum

"https://www.acmicpc.net/problem/1012 유기농 배추 <Silver II>"

Plant = Enum("Plant", "lettuce empty")

def calc_num_of_earthworm(plants, total_x, total_y):
    visited = [[False for _ in range(total_x)] for _ in range(total_y)]

    result = 0
    for start_y in range(total_y):
        for start_x in range(total_x):
            is_visited = not visited[start_y][start_x]
            if is_visited and plants[start_y][start_x] == Plant.lettuce:
                result += 1
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
                        is_lettuce = plants[dy][dx] == Plant.lettuce
                        if is_visited and is_lettuce:
                            visited[dy][dx] = True
                            queue.append((dx, dy))

    return result

num_of_case = int(stdin.readline())
for _ in range(num_of_case):
    plant_x, plant_y, num_of_plant = map(int, stdin.readline().split())
    plants = [
        [Plant.empty for _ in range(plant_x)]
        for _ in range(plant_y)
    ]

    for _ in range(num_of_plant):
        current_x, current_y = map(int, stdin.readline().split())
        plants[current_y][current_x] = Plant.lettuce

    print(calc_num_of_earthworm(plants, plant_x, plant_y))

