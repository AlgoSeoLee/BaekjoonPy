from sys import stdin

"https://www.acmicpc.net/problem/1918 후위 표기식 <Gold IV>"

def find_bracket_end(convert, start):
    bracket = 1
    forward_pos = start + 1
    forward = convert[forward_pos]
    while True:
        if forward == '(':
            bracket += 1
        elif forward == ')':
            bracket -= 1
            if bracket == 0:
                return forward_pos

        forward_pos += 1
        forward = convert[forward_pos]

def find_bracket_start(convert, end):
    bracket = 1
    prev_pos = end - 1
    prev = convert[prev_pos]
    while True:
        if prev == ')':
            bracket += 1
        elif prev == '(':
            bracket -= 1
            if bracket == 0:
                return prev_pos

        prev_pos -= 1
        prev = convert[prev_pos]

def preprocessing(plain):
    convert = list(plain)
    convert_length = len(convert)

    pos = 0
    while pos < convert_length:
        current = convert[pos]
        if current == '*' or current == '/':
            left = pos - 1
            right = pos + 1
            prev = convert[left]
            forward = convert[right]
            if right < convert_length and forward == '(':
                right = find_bracket_end(convert, right) - 1
            if left >= 0 and prev == ')':
                left = find_bracket_start(convert, left)

            convert.insert(right + 1, ')')
            convert.insert(left, '(')
            convert_length += 2
            pos += 1

        pos += 1

    return (convert, convert_length)

ALPHABET_START = ord('A')
ALPHABET_END = ord('Z')

def reverse_poland_expression(arr, arr_length):
    elem = ''
    ops = []
    pos = 0
    while pos < arr_length:
        current = arr[pos]
        ascii_code = ord(current)
        if ascii_code >= ALPHABET_START and ascii_code <= ALPHABET_END:
            elem += current
            pos += 1
        elif current == '(':
            start = pos
            end = find_bracket_end(arr, start)
            start += 1
            length = end - start
            elem += reverse_poland_expression(arr[start:end], length)
            pos = end
        elif current == ')':
            pos += 1
            continue
        else:
            ops.append(current)
            pos += 1
            continue

        try:
            elem += ops.pop()
        except IndexError:
            pass

    return elem + ''.join(reversed(ops))

arr, arr_length = preprocessing(stdin.readline().rstrip())
print(reverse_poland_expression(arr, arr_length))

