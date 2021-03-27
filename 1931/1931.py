from sys import stdin
from operator import itemgetter

"https://www.acmicpc.net/problem/1931 회의실 배정 <Silver II>"

num_of_meeting = int(stdin.readline())
meetings = []

for _ in range(num_of_meeting):
    meetings.append(tuple(map(int, stdin.readline().split())))

meetings.sort(key=itemgetter(1,0))

count = 0
end = 0
for m in meetings:
    if m[0] >= end:
        count += 1
        end = m[1]

print(count)
