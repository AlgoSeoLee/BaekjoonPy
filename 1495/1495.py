from sys import stdin

read_integers = lambda: map(int, stdin.readline().split())

num_of_song, start_volume, maximum_volume = read_integers()
volumes = list(read_integers())
dp = [[start_volume]]

for index in range(1, num_of_song + 1):
    prev = index - 1

    current = set()
    current_volume = volumes[prev]
    for prev_volume in dp[prev]:
        add = [
            prev_volume + current_volume,
            prev_volume - current_volume
        ]
        current.update(
            filter(lambda v: v <= maximum_volume and v >= 0, add)
        )
        
    dp.append(current)

try:
    result = max(dp[num_of_song])
    if result < 0 or result > maximum_volume:
        result = -1
except:
    result = -1
print(result)

