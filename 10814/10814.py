from sys import stdin

"https://www.acmicpc.net/problem/10814 나이순 정렬 <실버 5>"

n = int(stdin.readline())
member = {}
for _ in range(n):
    age, name = stdin.readline().split()
    age = int(age)
    if age not in member:
        member[age] = []

    member[age].append(name)

for k in sorted(member):
    for n in member[k]:
        print("{} {}".format(k, n))
