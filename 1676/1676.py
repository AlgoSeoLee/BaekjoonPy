from sys import stdin

"https://www.acmicpc.net/problem/1676 팩토리얼 0의 개수 <Silver III>"

def findZeroInFactorial(target):
    zeros = 0
    for i in range(target, 0, -1):
        while i % 5 == 0:
            i = i / 5
            zeros += 1

    return zeros

target = int(stdin.readline())
print(findZeroInFactorial(target))
