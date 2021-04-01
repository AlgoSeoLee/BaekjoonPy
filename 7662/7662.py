from sys import stdin
from heapq import heappush, heappop

"https://www.acmicpc.net/problem/7662 이중 우선순위 큐 <Gold V>"

for _ in range(int(stdin.readline())):
    largest = []
    smallest = []
    data = {}

    for _ in range(int(stdin.readline())):
        com, num = stdin.readline().split()
        num = int(num)

        if com == 'I':
            heappush(largest, -num)
            heappush(smallest, num)
            times = data.get(num)
            if times is None:
                times = 0

            data[num] = times + 1
        elif com == 'D':
            plus_minus = num * -1
            target = largest if plus_minus == -1 else smallest
            if len(data) == 0:
                continue

            try:
                index = plus_minus * heappop(target)
                while data.get(index) is None:
                    index = plus_minus * heappop(target)

                data[index] -= 1
                if data[index] == 0:
                    data.pop(index)

            except IndexError:
                continue

    if len(data) == 0:
        print("EMPTY")
        continue

    result = sorted(data.keys())
    print(result[-1], result[0])
