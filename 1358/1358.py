from sys import stdin
from math import sqrt

"https://www.acmicpc.net/problem/1358 하키 <Silver III>"

def calc_distance_between_points(source, destination):
    sx, sy = source
    dx, dy = destination

    return sqrt(pow(dx - sx,2) + pow(dy - sy,2))

def detect_persons_in_rink(width, height, rect_x, rect_y, persons):
    result = 0
    for (tx,ty) in persons:
        # 경기장의 직사각형 부분에 있는 경우를 탐지
        is_tx_in_rect = tx >= rect_x and tx <= rect_x + width
        is_ty_in_rect = ty >= rect_y and ty <= rect_y + height

        if is_tx_in_rect and is_ty_in_rect:
            result += 1
        # x 범위에 없더라도 만약에 y가 범위안에 존재한다면 양쪽 원에 있을 가능성이 있다.
        elif is_ty_in_rect:
            radius = height / 2

            oy = rect_y + radius
            left_right_x = [rect_x, rect_x + width]
            for ox in left_right_x:
                distance = calc_distance_between_points((ox, oy),(tx,ty))
                if distance <= radius:
                    result += 1
                    break

    return result

# 문제의 상수를 받는다.
width, height, rect_x, rect_y, num_of_person = map(
    int, stdin.readline().split()
)

# 사람의 좌표를 받는다.
persons = [
    list(map(int, stdin.readline().split()))
    for _ in range(num_of_person)
]

# 경기장 안에 있는 사람 수를 출력한다.
print(detect_persons_in_rink(width, height, rect_x, rect_y, persons))

