from sys import stdin

"https://www.acmicpc.net/problem/14171 Cities and States <Silver I>"

diff = {}

num_of_city = int(stdin.readline())
result = 0
for _ in range(num_of_city):
    city, state = stdin.readline().split()
    start_of_city = city[:2]

    if state != start_of_city:
        same_start_city = diff.get(start_of_city)
        if same_start_city and state in same_start_city:
            result += 1

    same_state = diff.get(state)
    if same_state == None:
        same_state = set()
        diff[state] = same_state
    same_state.add(start_of_city)

print(result)

