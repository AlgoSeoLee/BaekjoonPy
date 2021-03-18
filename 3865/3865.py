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
        academies[academy_name] = set(academy)

    result = set()
    queue = academies[target]
    while len(queue) != 0:
        name = queue.pop()
        try:
            next_academy = academies[name]
            queue = queue.union(next_academy)
        except KeyError:
            result.add(name)

    print(len(result))
