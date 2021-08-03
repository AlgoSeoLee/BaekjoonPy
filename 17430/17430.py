from sys import stdin

input_integer = lambda: int(stdin.readline())
input_coordinate = lambda: tuple(map(int, stdin.readline().split()))

num_of_case = input_integer()
for _ in range(num_of_case):
    num_of_coordinate = input_integer()

    coordinates = set()
    for _ in range(num_of_coordinate):
        coordinates.add(input_coordinate())

    balanced = True
    for x, y in coordinates:
        rev_x_test = (-x, y)
        rev_y_test = (x, -y)
        if rev_x_test in coordinates or rev_y_test in coordinates:
            continue

        balanced = False
        break

    if balanced:
        print("BALANCED")
    else:
        print("NOT BALANCED")

