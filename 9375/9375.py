from sys import stdin

num_of_test = int(stdin.readline())

for _ in range(num_of_test):
    num_of_wear = int(stdin.readline())
    wears = {}
    for _ in range(num_of_wear):
        name, part = stdin.readline().split()
        if wears.get(part) == None:
            wears[part] = 0
        wears[part] += 1

    num_of_case = 1
    for part in wears:
        num_of_case *= wears[part] + 1

    print(num_of_case - 1)

