def solution(numbers, target):
    answer = 0
    stack = []
    length = len(numbers)

    stack.append((numbers[0], 1))
    stack.append((-numbers[0], 1))

    while stack:
        current, level = stack.pop()

        directions = [
            (current + numbers[level], level + 1),
            (current - numbers[level], level + 1)
        ]

        for d in directions:
            new_target, new_level = d
            if new_level == length:
                if new_target == target:
                    answer += 1
            else:
                stack.append(d)

    return answer

print(solution([1,1,1,1,1], 3))
