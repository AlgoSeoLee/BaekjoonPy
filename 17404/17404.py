from sys import stdin, maxsize
from enum import Enum

"https://www.acmicpc.net/problem/17404 RGB거리 2 <Gold IV>"

RGB = Enum("RGB", "Red Green Blue")
FULL_COLOR = set(RGB)

num_of_house = int(stdin.readline())

input_painting_costs = lambda: {
    color: cost
    for color, cost in zip(list(RGB), map(int, stdin.readline().split()))
}

new_dp_data = lambda: {color: maxsize for color in list(RGB)}

dp = {}

first_line = input_painting_costs()
for c in list(RGB):
    init = new_dp_data()
    init[c] = first_line[c]
    dp[c] = [init]

for i in range(1, num_of_house):
    costs = input_painting_costs()
    for start_color in list(RGB):
        line = new_dp_data()
        color_pool = FULL_COLOR
        if i == num_of_house - 1:
            color_pool = color_pool - {start_color}

        for current_color in color_pool:
            selectable_color = color_pool - {current_color}

            current_cost = min(
                map(lambda c: dp[start_color][i - 1][c], selectable_color)
            )
            if current_cost != maxsize:
                current_cost += costs[current_color]
                line[current_color] = current_cost

        dp[start_color].append(line)

min_cost = maxsize
for color in list(RGB):
    min_cost = min(min_cost, min(dp[color][num_of_house - 1].values()))

print(min_cost)

