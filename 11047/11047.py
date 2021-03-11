from sys import stdin

"https://www.acmicpc.net/problem/11047 동전 0 <Silver II>"

types, won = map(int, stdin.readline().split())

coins = []
for _ in range(types):
	coins.append(int(stdin.readline().rstrip()))

each = 0
for c in sorted(coins, reverse=True):
	each = each + won // c
	won = won % c

print(each)
