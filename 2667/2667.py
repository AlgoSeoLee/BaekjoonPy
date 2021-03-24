from sys import stdin
from queue import Queue

def _BFS(matrix, visited, size, x, y):
    queue = Queue()

    if matrix[y][x] and not visited[y][x]:
        queue.put((x, y))
        visited[y][x] = True

    connected = 0
    while not queue.empty():
        x, y = queue.get()
        connected += 1

        diff = []
        if x > 0:
            diff.append((-1, 0))

        if y > 0:
            diff.append((0, -1))

        maximum = size - 1

        if x < maximum:
            diff.append((1, 0))

        if y < maximum:
            diff.append((0, 1))

        for dx, dy in diff:
            tx = x + dx
            ty = y + dy
            if matrix[ty][tx] and not visited[ty][tx]:
                visited[ty][tx] = True
                queue.put((tx, ty))

    return connected

def matrix_travel(matrix, size):
    visited = [[False for _ in range(size)] for _ in range(size)]
    result = []
    for y in range(size):
        for x in range(size):
            connected = _BFS(matrix, visited, size, x, y)
            if connected > 0:
                result.append(connected)

    return sorted(result)

country = []
country_size = int(stdin.readline())

for _ in range(country_size):
    line = list(map(lambda c: c == '1', stdin.readline().rstrip()))
    country.append(line)

result = matrix_travel(country, country_size)
print(len(result))
for r in result:
    print(r)
