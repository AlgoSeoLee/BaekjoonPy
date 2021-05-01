from sys import stdin

"https://www.acmicpc.net/problem/2579 계단 오르기 <Silver III>"

num_of_stair = int(stdin.readline())
stairs = [int(stdin.readline()) for _ in range(num_of_stair)]
stairs.insert(0, 0)
scores = [0 for _ in range(num_of_stair + 1)]

scores[1] = stairs[1]
if num_of_stair > 1:
    scores[2] = sum(stairs[1:3]);

for i in range(3, num_of_stair+1):
    scores[i] = max([
        # jump
        scores[i - 2] + stairs[i],
        # continue
        scores[i - 3] + sum(stairs[i-1:i+1])
    ])

print(scores[num_of_stair])

