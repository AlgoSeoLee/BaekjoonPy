from sys import stdin
from heapq import heappush, heappop

"https://www.acmicpc.net/problem/11279 최대 힙 <Silver II>"

heap = []
num_of_command = int(stdin.readline())

for _ in range(num_of_command):
    command = int(stdin.readline())
    if command == 0:
        smallest = 0
        try:
            smallest = -1 * heappop(heap)
        except IndexError:
            pass

        print(smallest)
    else:
        heappush(heap, -1 * command)
