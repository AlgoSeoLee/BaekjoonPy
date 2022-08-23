from sys import stdin

numbers = [int(stdin.readline()) for _ in range(int(stdin.readline()))]

stack = [[set([i + 1]), set([j])] for i, j in enumerate(numbers)]

maximum_combination = set()

while stack:
    ordered, random = stack.pop()

    at_ordered = random - ordered
    at_random = ordered - random

    next_targets = []

    if not at_ordered and not at_random:
        same_combination = set()
        for zero_index, number_of_random in enumerate(numbers):
            number_of_ordered = zero_index + 1
            if number_of_random == number_of_ordered:
                same_combination.add(number_of_ordered)

        combination = ordered | same_combination

        if len(combination) > len(maximum_combination):
            maximum_combination = combination
        continue

    if at_random:
        for zero_index, number_of_random in enumerate(numbers):
            if number_of_random in at_random:
                number_of_ordered = zero_index + 1
                next_targets.append(
                        [
                            ordered | set([number_of_ordered]),
                            random | set([number_of_random])
                            ]
                        )

    if at_ordered:
        for number_of_ordered in at_ordered:
            zero_index = number_of_ordered - 1
            target_random = numbers[zero_index]
            next_targets.append(
                    [
                        ordered | set([number_of_ordered]),
                        random | set([target_random])
                    ]
            )

    stack.extend(next_targets)

print(len(maximum_combination))
for num in maximum_combination:
    print(num)
