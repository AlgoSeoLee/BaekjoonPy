from sys import stdin

num_of_pages, num_of_ops = map(int, stdin.readline().split())

current_page = None
backward_history = []
forward_history = []

for _ in range(num_of_ops):
    line = stdin.readline().split()

    ops = line[0]
    if ops == 'A':
        forward_history = []
        page = line[1]
        if current_page != None:
            backward_history.append(current_page)
        current_page = page
    elif ops == 'B':
        if len(backward_history) != 0:
            forward_history.append(current_page)
            current_page = backward_history.pop()
    elif ops == 'F':
        if len(forward_history) != 0:
            backward_history.append(current_page)
            current_page = forward_history.pop()
    elif ops == 'C':
        if len(backward_history) != 0:
            compressed = []
            for h in backward_history:
                if not compressed or h != compressed[-1]:
                    compressed.append(h)

            backward_history = compressed

print(current_page)
if backward_history:
    print(*reversed(backward_history))
else:
    print(-1)
if forward_history:
    print(*reversed(forward_history))
else:
    print(-1)
