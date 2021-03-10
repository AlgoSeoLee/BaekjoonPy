from sys import stdin

n, m = map(int, stdin.readline().split())

NotSeen = {}
for _ in range(n):
    NotSeen[stdin.readline().rstrip()] = True

nobody = []
for _ in range(m):
    NotHear = stdin.readline().rstrip()
    if NotHear in NotSeen:
        nobody.append(NotHear)

print(len(nobody))
for name in sorted(nobody):
    print(name)
