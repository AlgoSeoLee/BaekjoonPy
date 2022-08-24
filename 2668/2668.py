from sys import stdin

numbers = [int(stdin.readline()) for _ in range(int(stdin.readline()))]

maximum_comb = set()

stack = [[i] for i in range(len(numbers), 0, -1)]
while stack:
    cycle = stack.pop()
    visited = set(cycle[:-1])
    latest = cycle[-1]
    if latest in visited:
        start = 0
        for index in range(len(numbers)):
            start = index
            if cycle[index] == latest:
                break
        maximum_comb |= set(cycle[start:])
        continue

    next_of_cycle = numbers[latest - 1]
    cycle.append(next_of_cycle)

    stack.append(cycle)

print(len(maximum_comb))
for element in sorted(maximum_comb):
    print(element)
