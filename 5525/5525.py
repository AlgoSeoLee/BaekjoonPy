from sys import stdin

"https://www.acmicpc.net/problem/5525 IOIOI <Silver II>"

num_of_O = int(stdin.readline())
length_of_plain = int(stdin.readline())
plain = stdin.readline()

condition = 'I' + 'OI' * num_of_O

level = 0
maximum_level = len(condition) - 1
multiple_O = num_of_O > 1
result = 0
started_at = 0
position = 0
while position < length_of_plain:
    current = plain[position]
    target = condition[level]
    if current == target:
        if multiple_O and level == 0:
            started_at = position

        if level == maximum_level:
            level = 1
            result += 1
            if multiple_O:
                started_at = started_at + 2
                next_phase = started_at + maximum_level + 1
                if next_phase > length_of_plain:
                    break
                position = started_at
        else:
            level += 1
    elif current == 'I':
        started_at = position
        level = 1
    else:
        level = 0

    position += 1

print(result)

