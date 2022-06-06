from sys import stdin, maxsize
from heapq import heappop, heappush

visited = {}
def calc_minimum_resort_cost(days, num_of_days):
    visited = {}
    queue = [(0, 0, 0)]

    while queue:
        current = heappop(queue)
        if visited.get(current):
            continue

        idx, cost, coupon = current
        if idx >= num_of_days:
            return cost
        elif not days[idx]:
            heappush(queue, (idx + 1, cost, coupon))

        visited[current] = True

        heappush(queue, (idx + 5, cost + 37, coupon + 2))
        heappush(queue, (idx + 3, cost + 25, coupon + 1))
        if coupon > 2:
            heappush(queue, (idx + 1, cost, coupon - 3))
        else:
            heappush(queue, (idx + 1, cost + 10, coupon))

num_of_days, _ = map(int, stdin.readline().split())
days = [True for _ in range(num_of_days)]
for schedule in map(int, stdin.readline().split()):
    days[schedule - 1] = False

print(calc_minimum_resort_cost(days, num_of_days) * 1000)
