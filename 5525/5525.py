from sys import stdin

"https://www.acmicpc.net/problem/5525 IOIOI <Silver II>"

num_of_O = int(stdin.readline())
stdin.readline()
plain = stdin.readline()

condition = 'I' + 'OI' * num_of_O

level = 0
maximum_level = len(condition) - 1
result = 0

for current in plain:
    target = condition[level]
    if current == target:
        if level == maximum_level:
            level = 1
            result += 1
        else:
            level += 1
    elif target == 'I':
        level = 1
    else:
        level = 0

print(result)

