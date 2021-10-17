from sys import stdin, maxsize

"https://www.acmicpc.net/problem/12852 1로 만들기 2 <Silver I>"

def solve_to_1(target):
    operations = [
        lambda x: x // 2 if x % 2 == 0 else None,
        lambda x: x - 1,
        lambda x: x // 3 if x % 3 == 0 else None,
    ]

    stack = []
    visited = {}

    stack.append((1, target, set([target])))
    visited[target] = 1

    minimum = maxsize
    minimum_trail = None

    while stack:
        level, x, trail = stack.pop()
        next_level = level + 1
        if x == 1 and level < minimum:
            minimum = level
            minimum_trail = sorted(trail, reverse=True)
            continue

        steps = map(lambda ops: ops(x), operations)
        steps = filter(
            lambda s:
                s != None and
                (visited.get(s) == None or visited[x] >= next_level),
            steps
        )
        steps = map(lambda s: (next_level, s, trail.union([s])), steps)

        for st in steps:
            _, s, _ = st
            
            visited[s] = next_level
            stack.append(st)

    return minimum_trail

target = int(stdin.readline())
print(*solve_to_1(target))
