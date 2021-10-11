from sys import stdin
from heapq import heappop, heappush

"https://www.acmicpc.net/problem/1715 카드 정렬하기 <Gold IV>"

read_integer = lambda: int(stdin.readline())

num_of_deck = read_integer()
decks = []

for _ in range(num_of_deck):
    heappush(decks, read_integer())

counting = 0

if num_of_deck != 1:
    while decks:
        d = heappop(decks)
        d += heappop(decks)
        counting += d
        if len(decks) > 0:
            heappush(decks, d)

print(counting)

