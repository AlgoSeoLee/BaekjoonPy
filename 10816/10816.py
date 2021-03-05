from sys import stdin

"https://www.acmicpc.net/problem/10816 숫자 카드 2 <실버 4>"

def arrayFromLine():
    return map(int, stdin.readline().split())

stdin.readline()
deck = {}
for i in arrayFromLine():
    if i not in deck:
        deck[i] = 0;

    deck[i] = deck[i] + 1

stdin.readline()
for i in arrayFromLine():
    each = 0
    if i in deck:
        each = deck[i]

    print(each, end=' ')
