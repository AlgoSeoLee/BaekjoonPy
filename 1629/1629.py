from sys import stdin

"https://www.acmicpc.net/problem/1629 곱셈 <Silver I>"

# 파이썬 자체의 최적화를 믿으세요! 파멘!

target, times, mod = map(int, stdin.readline().split())
print(pow(target, times, mod))

