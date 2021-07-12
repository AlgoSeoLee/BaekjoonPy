from sys import stdin

# referenced code by https://www.acmicpc.net/board/view/31149
# also translated js to python

def compare(a, b, c, d):
    if b == c or a == d:
        return 1
    elif b < c or d < a:
        return 0
    return 2

for _ in range(4):
    data = [int(v) for v in stdin.readline().split()]
    a_start_x, a_start_y, a_end_x, a_end_y = data[:4]
    b_start_x, b_start_y, b_end_x, b_end_y = data[4:]

    result = compare(a_start_x, a_end_x, b_start_x, b_end_x)
    result *= compare(a_start_y, a_end_y, b_start_y, b_end_y)

    if result == 4:
        print('a')
    elif result == 2:
        print('b')
    elif result == 1:
        print('c')
    else:
        print('d')


