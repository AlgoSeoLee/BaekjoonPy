from sys import stdin

pairs = {}

num_of_city = int(stdin.readline())
result = 0
for _ in range(num_of_city):
    state, code = stdin.readline().split()
    if pairs.get(code):
        result += 1

    pairs[code] = state

print(result)

