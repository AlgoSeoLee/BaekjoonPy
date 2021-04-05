from sys import stdin

def check_one_color(paper):
    colors = set()
    invalid = False
    for line in paper:
        colors = colors.union(set(line))
        if len(colors) != 1:
            invalid = True
            break;

    return not invalid

def slice_paper(paper, size):
    div3 = size // 3

    red = 0
    white = 0
    blue = 0

    for y in range(0, size, div3):
        y_slice = paper[y:y+div3]
        for x in range(0, size, div3):
            cutting_paper = []
            for line in y_slice:
                cutting_paper.append(line[x:x+div3])

            if check_one_color(cutting_paper):
                color = cutting_paper[0][0]
                if color == -1:
                    red += 1
                elif color == 0:
                    white += 1
                else:
                    blue += 1
            else:
                r, w, b = slice_paper(cutting_paper, div3)
                red += r
                white += w
                blue += b

    return (red, white, blue)

size = int(stdin.readline())
paper = [list(map(int, stdin.readline().split())) for _ in range(size)]

result = None
if check_one_color(paper):
    result = [0, 0, 0]
    color = paper[0][0] + 1
    result[color] = 1
else:
    result = slice_paper(paper, size)

for r in result:
    print(r)
