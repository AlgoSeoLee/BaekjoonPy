from sys import stdin
import re

"https://www.acmicpc.net/problem/3865 학회원 <Gold IV>"

SPLIT = re.compile(r"[:,]")

while True:
    number_of_academy = int(stdin.readline())
    if number_of_academy == 0:
        break

    academies = {}
    target = None
    for _ in range(number_of_academy):
        line = stdin.readline().rstrip()[:-1]

        academy = SPLIT.split(line)
        academy_name = academy[0]
        academy = academy[1:]

        if len(academies) == 0:
            target = academy_name
        academies[academy_name] = academy

    result = set()
    visited = set()

    queue = set(academies[target])
    visited.add(target)

    while queue:
        name = queue.pop()
        next_academy = academies.get(name)
        if next_academy:
            next_academy = filter(
                lambda a: not a in visited,
                next_academy
            )
            for n in next_academy:
                queue.add(n)
                visited.add(n)
        else:
            result.add(name)

    print(len(result))
