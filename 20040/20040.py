# https://www.acmicpc.net/problem/20040 '사이클 게임' 골드 4
from sys import stdin

num_of_point, num_of_turn = map(int, stdin.readline().split())

game = [i for i in range(num_of_point)]

def findRoot(point):
    while (point != game[point]):
        point = game[point]
    return point

def checkCycle(source, destination):
    root_of_source = findRoot(source)
    root_of_destination = findRoot(destination)

    if (root_of_source != root_of_destination):
        return False

    return True

def unionLine(source, destination):
    root_of_source = findRoot(source)
    root_of_destination = findRoot(destination)
    if root_of_source < root_of_destination:
        game[root_of_destination] = root_of_source
    else:
        game[root_of_source] = root_of_destination

when_game_end = 0
for turn in range(num_of_turn):
    source, destination = map(int, stdin.readline().split())
    if checkCycle(source, destination):
        when_game_end = turn + 1
        break
    unionLine(source, destination)

print(when_game_end)
