from sys import stdin, setrecursionlimit

setrecursionlimit(8000)

read_integers = lambda: [int(v) for v in stdin.readline().split()]

MAXIMUM = 2001
dp = [[-1 for _ in range(MAXIMUM)] for _ in range(MAXIMUM)]
def solve_cardgame(
    num_of_cards,
    left_deck, right_deck,
    left_index, right_index):

    solve = lambda l, r: solve_cardgame(
        num_of_cards, left_deck, right_deck,
        l, r
    )

    if left_index >= num_of_cards or right_index >= num_of_cards:
        return 0

    result = dp[left_index][right_index]
    left = left_deck[left_index]
    right = right_deck[right_index]
    if result != -1:
        pass
    elif left > right:
        result = right + solve(left_index, right_index + 1)
    else:
        discard_left = solve(left_index + 1, right_index)
        discard_both = solve(left_index + 1, right_index + 1)
        result = max(discard_left, discard_both)

    dp[left_index][right_index] = result
    return result

num_of_cards = int(stdin.readline())
left_deck = read_integers()
right_deck = read_integers()

print(solve_cardgame(num_of_cards, left_deck, right_deck, 0, 0))

