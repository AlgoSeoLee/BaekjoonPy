from sys import stdin
from heapq import heappush, heappop

"https://www.acmicpc.net/problem/11000 강의실 배정 <Gold V>"

num_of_lecture = int(stdin.readline())

lectures = []
for _ in range(num_of_lecture):
    lectures.append(tuple(int(hour) for hour in stdin.readline().split()))
lectures.sort()

new_classroom = lambda lec: tuple(reversed(lec))

classrooms = [new_classroom(lectures[0])]
num_of_classroom = 1
for lec in lectures[1:]:
    lec_start, _ = lec
    classroom_end, _ = classrooms[0]

    if classroom_end > lec_start:
        num_of_classroom += 1
        heappush(classrooms, new_classroom(lec))
    else:
        heappop(classrooms)
        heappush(classrooms, new_classroom(lec))

print(num_of_classroom)
