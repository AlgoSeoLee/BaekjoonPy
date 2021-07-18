from sys import stdin

"https://www.acmicpc.net/problem/15973 두 박스 <Silver I>"

# referenced code by https://www.acmicpc.net/board/view/31149
# also translated js to python

def compare(a, b, c, d):
    if b == c or a == d:
        return 1
    elif b < c or d < a:
        return 0
    return 2

def read_int():
    return map(int, stdin.readline().split())

a_start_x, a_start_y, a_end_x, a_end_y = read_int()
b_start_x, b_start_y, b_end_x, b_end_y = read_int()

result = compare(a_start_x, a_end_x, b_start_x, b_end_x)
result *= compare(a_start_y, a_end_y, b_start_y, b_end_y)

if result == 4:
    print('FACE')
elif result == 2:
    print('LINE')
elif result == 1:
    print('POINT')
else:
    print('NULL')

