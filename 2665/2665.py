from sys import stdin
from heapq import heappush,heappop

size_of_board = int(stdin.readline())
board = [
	[c == '1' for c in stdin.readline().rstrip()]
	for _ in range(size_of_board)
]

queue = [(0, 0, 0)]
visited = {}
while queue:
	changes, x, y = heappop(queue)

	if x + 1 == size_of_board and y + 1 == size_of_board:
		print(changes)
		break

	when_visited = visited.get((x,y))
	if when_visited is not None and changes >= when_visited:
		continue

	visited[(x,y)] = changes

	ways = []
	if x > 0:
		ways.append((x-1,y))
	if y > 0:
		ways.append((x,y-1))
	if x < size_of_board - 1:
		ways.append((x+1,y))
	if y < size_of_board - 1:
		ways.append((x,y+1))

	for target_x, target_y in ways:
		is_black = not board[target_y][target_x]
		heappush(
			queue,
			(changes + 1 if is_black else changes, target_x, target_y)
		)

