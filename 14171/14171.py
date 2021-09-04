from sys import stdin

"https://www.acmicpc.net/problem/14171 Cities and States <Silver I>"

num_of_city = int(stdin.readline())

same = {}
result = 0
for _ in range(num_of_city):
    city, state = stdin.readline().split()
    city = city[:2]

    if city == state:
        continue

    if same.get((city, state)) == None:
        same[(city, state)] = 0
    same[(city, state)] += 1

    if same.get((state, city)) != None:
        result += same[(state, city)]

print(result)
