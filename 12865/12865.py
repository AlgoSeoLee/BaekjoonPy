from sys import stdin

def solve_knapsack(items, num_of_item, weight_limit):
    dp = [
        [0 for _ in range(0, weight_limit+1)]
        for _ in range(0,num_of_item+1)
    ]
    for item_index in range(1, num_of_item+1):
        item_weight, item_value = items[item_index - 1]
        for weight in range(1, weight_limit+1):
            current = None
            if item_weight > weight:
                current = dp[item_index-1][weight]
            else:
                current = max(
                    dp[item_index-1][weight],
                    dp[item_index-1][weight - item_weight] + item_value
                )

            dp[item_index][weight] = current

    return dp[num_of_item][weight_limit]

num_of_item, weight_limit = map(int, stdin.readline().split())
items = [
    [int(v) for v in stdin.readline().split()]
    for _ in range(num_of_item)
]
print(solve_knapsack(items, num_of_item, weight_limit))
