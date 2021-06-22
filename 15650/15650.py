from sys import stdin

"https://www.acmicpc.net/problem/15650 N과 M (2) <Silver III>"

def solve_sequence(limit, length_of_seq):
    if length_of_seq == limit:
        return [[i for i in range(limit)]]

    result = []
    for i in range(limit - length_of_seq + 1):
        if length_of_seq == 1:
            result.append([i])
            continue

        seq = []
        visited = []
        for t in range(limit):
            current = False
            if t < i:
                current = True
            visited.append(current)

        stack = []
        start = i + 1
        stack.append(([i], 1))
        while stack:
            sub_seq, level = stack.pop()
            current = sub_seq[-1]
            if visited[current]:
                continue
            else:
                visited[current] = True

            directions = filter(
                lambda x: not visited[x],
                range(limit - 1, -1, -1)
            )

            data = map(
                lambda d: (sub_seq + [d], level + 1),
                directions
            )

            for d in data:
                if d[1] == length_of_seq:
                    result.append(sorted(d[0]))
                    continue
                stack.append(d)

    return sorted(result)

N, M = map(int, stdin.readline().split())
result = solve_sequence(N, M)
for line in result:
    for number in map(lambda x: x + 1, line):
        print(number, end=' ')
    print()
