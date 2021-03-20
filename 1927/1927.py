from sys import stdin
from heapq import heappush, heappop

heap = []
num_of_command = int(stdin.readline())

for _ in range(num_of_command):
    command = int(stdin.readline())
    if command == 0:
        smallest = 0
        try:
            smallest = heappop(heap)
        except IndexError:
            pass

        print(smallest)
    else:
        heappush(heap, command)
