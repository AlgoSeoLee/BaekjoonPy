from sys import stdin

stdin.readline()
waiting = [int(s) for s in stdin.readline().split()]
waiting.sort()

spent_time = 0
waiting_time = 0
for process_time in waiting:
    waiting_time += process_time
    spent_time += waiting_time

print(spent_time)
