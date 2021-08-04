from sys import stdin

input_integers = lambda: map(int, stdin.readline().split())

translate_equation = lambda a, b: -(a / b)
detect_collision = lambda A, a1, a2: A > a1 and A < a2

X, Y, C = input_integers()
x1, x2, y1, y2 = input_integers()
is_lucky = True
if Y != 0 and X != 0:
    X = translate_equation(X, Y)
    C = translate_equation(C, Y)
    equation = lambda x: X * x + C

    for i in range(x1, x2+1):
        current = equation(i)
        if detect_collision(current, y1, y2):
            is_lucky = False
            break
else:
    if Y == 0:
        X = translate_equation(C, X)
        if detect_collision(X, x1, x2):
            is_lucky = False
    elif X == 0:
        Y = translate_equation(C, Y)
        if detect_collision(Y, y1, y2):
            is_lucky = False

if is_lucky:
    print("Lucky")
else:
    print("Poor")
