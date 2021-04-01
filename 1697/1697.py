from sys import stdin

"https://www.acmicpc.net/problem/1697 숨바꼭질 <Silver I>"

def hide_and_seek(origin, target):
    queue = []
    visited = [False for i in range(100001)]

    if origin == target:
        return 0
    queue.append((origin, 0))
    visited[origin] = True

    while len(queue) != 0:
        position, current = queue.pop()

        new_positions = []

        if position != 0:
            new_positions.append(position - 1)
        if position != 100000:
            new_positions.append(position + 1)
        if position <= 50000:
            new_positions.append(position * 2)

        ops = current + 1
        for p in new_positions:
            if p == target:
                return ops
            elif not visited[p]:
                visited[p] = True
                queue.insert(0, (p, ops))

origin, target = map(int, stdin.readline().split())
print(hide_and_seek(origin, target))
