from sys import stdin
from collections import deque

num_of_lecture = int(stdin.readline())

lectures = []
for _ in range(num_of_lecture):
    lectures.append(tuple(int(hour) for hour in stdin.readline().split()))
lectures.sort()

classes = deque()
num_of_class = 0
for lec_start, lec_end in lectures:
    if num_of_class == 0:
        num_of_class += 1
        classes.append(lec_end)
    else:
        is_replace = False
        is_complete = False
        for class_idx in range(num_of_class - 1):
            current = classes[class_idx]
            if current <= lec_start:
                classes.remove(current)
                is_replace = True

            if is_replace and classes[class_idx] >= lec_end:
                classes.insert(class_idx, lec_end)
                is_complete = True
                break

        if not is_complete:
            position = num_of_class - 1
            if is_replace:
                position -= 1

            if classes[position] > lec_end:
                classes.insert(position, lec_end)
            else:
                if not is_replace:
                    num_of_class += 1
                classes.append(lec_end)

print(num_of_class)
