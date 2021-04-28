from sys import stdin

def findZeroInFactorial(target):
    zeros = 0
    for i in range(target, 0, -1):
        while i % 5 == 0:
            i = i / 5
            zeros += 1

    return zeros

target = int(stdin.readline())
print(findZeroInFactorial(target))
