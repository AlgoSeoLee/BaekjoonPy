from sys import stdin
from enum import Enum

"https://www.acmicpc.net/problem/1149 RGB거리 <Silver I>"

RGB = Enum("RGB", "red green blue")

num_of_house = int(stdin.readline())
paint_cost_table = []

for _ in range(num_of_house):
    color_to_cost = {}
    color_to_cost.update(
        zip(RGB, map(int, stdin.readline().split()))
    )
    paint_cost_table.append(color_to_cost)

dp = [
    {
        RGB.red: 0,
        RGB.green: 0,
        RGB.blue: 0,
    }
]

for i in range(num_of_house):
    prev = dp[i]
    current_cost = {
        RGB.red: min(prev[RGB.green], prev[RGB.blue]),
        RGB.green: min(prev[RGB.red], prev[RGB.blue]),
        RGB.blue: min(prev[RGB.green], prev[RGB.red])
    }
    for color in RGB:
        current_cost[color] += paint_cost_table[i][color]
    dp.append(current_cost)

print(min(dp[num_of_house].values()))
