from sys import stdin

size, days = map(int, stdin.readline().split())

honeycomb = [[1 for _ in range(size)] for _ in range(size)]

for _ in range(days):
    zero, one, two = map(int, stdin.readline().split())
    increase_speeds = list()
    increase_speeds.extend([0 for _ in range(zero)])
    increase_speeds.extend([1 for _ in range(one)])
    increase_speeds.extend([2 for _ in range(two)])
    increase_matrix = [[0 for _ in range(size)] for _ in range(size)]
    max_speed = 0

    for i in range(size):
        current_speed = increase_speeds[i]
        increase_matrix[size - 1 - i][0] = current_speed
        honeycomb[size - 1 - i][0] += current_speed

    for i in range(size - 1):
        current_speed = increase_speeds[size + i]
        increase_matrix[0][i + 1] = current_speed
        honeycomb[0][i + 1] += current_speed

    for x in range(1, size):
        for y in range(1, size):
            current_speed = max(
                    increase_matrix[y-1][x],
                    increase_matrix[y-1][x-1],
                    increase_matrix[y][x-1])
            if current_speed > max_speed:
                max_speed = current_speed
            increase_matrix[y][x] = max_speed
            honeycomb[y][x] += max_speed 

for line in honeycomb:
    print(*line)
