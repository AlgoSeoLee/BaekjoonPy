from sys import stdin
from collections import deque

read_integers = lambda: map(int, stdin.readline().split())

num_of_song, start_volume, maximum_volume = read_integers()
volumes = deque(read_integers())
volumes.appendleft(start_volume)
dp = [[start_volume, start_volume, start_volume]]

for index in range(1, num_of_song + 1):
    prev = index - 1

    prev_max_volume = max(dp[prev])
    prev_min_volume = min(dp[prev])
    cur_volume = volumes[index]

    current = [0, 0]

    current = [
        prev_min_volume - cur_volume,
        prev_max_volume + cur_volume,
        prev_max_volume - cur_volume
    ]
    if current[1] > maximum_volume:
        current[1] = prev_min_volume + cur_volume

    if current[0] < 0:
        current[0] = prev_max_volume - cur_volume

    dp.append(current)

result = max(dp[num_of_song])
if result < 0 or result > maximum_volume:
    result = -1
print(dp)
print(result)

