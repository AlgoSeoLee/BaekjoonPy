from sys import stdin

while True:
    line = stdin.readline().rstrip()
    if line == ".":
        break

    stack = []
    invalid = False
    for c in line:
        if c == '[' or c == '(':
            stack.append(c)
            continue

        check = None
        if c == ']':
            check = '['
        elif c == ')':
            check = '('
        else:
            continue

        try:
            recent = stack.pop()
            if recent != check:
                invalid = True
                break
        except IndexError:
            invalid = True
            break

    result = "yes"
    if invalid or len(stack) != 0:
        result = "no"

    print(result)
