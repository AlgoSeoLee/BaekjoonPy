from sys import stdin

"https://www.acmicpc.net/problem/2630 색종이 만들기 <Silver III>"

def isDiff(target):
    diff = False
    tester = None
    for l in target:
        if not diff:
            for c in l:
                if tester is None:
                    tester = c
                elif tester is not c:
                    diff = True
                    break

    return (diff, tester)

def cutPaper(paper, x, y, size):
    half = size // 2
    white = 0
    blue = 0

    for i in range(y, size, half):
        line = paper[i:i+half]
        for j in range(x, size, half):
            cutting = []
            for l in line:
                cutting.append(l[j:j+half])

            diff, tester = isDiff(cutting)

            if diff:
                w, b = cutPaper(cutting, 0, 0, half)
                white += w
                blue += b
            else:
                if tester:
                    blue += 1
                else:
                    white += 1

    return (white, blue)

size = int(stdin.readline())
paper = []

for _ in range(size):
    paper.append(list(map(lambda x: x == '1', stdin.readline().split())))

diff, target = isDiff(paper)
result = None
if not diff:
    result = [1, 0]
    if target:
        result = [0, 1]
else:
    result = cutPaper(paper, 0, 0, size)

for r in result:
    print(r)
