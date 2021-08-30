from sys import stdin

read_integers = lambda: map(int, stdin.readline().split())

num_of_people = int(stdin.readline())
people = []

for _ in range(num_of_people):
    people.append(tuple(read_integers()))

ranking = []
for i in range(num_of_people):
    pos = 1
    current = people[i]
    for j in range(num_of_people):
        if i == j:
            continue

        target = people[j]

        condition = current[0] < target[0]
        condition = condition and current[1] < target[1]
        if condition:
            pos += 1

    ranking.append(pos)

for rank in ranking:
    print(rank, end=' ')
print()
