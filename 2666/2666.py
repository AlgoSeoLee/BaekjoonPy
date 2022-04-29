from sys import stdin, maxsize
from collections import deque

num_of_closet = int(stdin.readline())
where_is_already_open = [int(v) for v in stdin.readline().split()]
num_of_open_door = int(stdin.readline())
to_open_doors = [int(stdin.readline()) for _ in range(num_of_open_door)]

# where_is_open, num_of_move_door, step
queue = deque([(where_is_already_open, 0, 0)])
minimum_move_door = maxsize

while queue:
    where_is_open, num_of_move_door, step = queue.popleft()
    if step == num_of_open_door:
        minimum_move_door = min(minimum_move_door, num_of_move_door)
        continue

    open_target = to_open_doors[step]
    distance_between = map(lambda cur:abs(cur - open_target),where_is_open)
    distance_between = list(distance_between)

    step += 1

    for dist, i in zip(distance_between, range(len(distance_between))):
        next_where_is_open = where_is_open.copy()
        next_where_is_open[i] = open_target
        queue.append((next_where_is_open, num_of_move_door + dist, step))

print(minimum_move_door)
