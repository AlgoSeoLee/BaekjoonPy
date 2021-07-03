from sys import stdin

# 파이썬 자체의 최적화를 믿으세요! 파멘!

target, times, mod = map(int, stdin.readline().split())
print(pow(target, times, mod))

