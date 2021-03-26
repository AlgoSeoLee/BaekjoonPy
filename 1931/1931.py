from sys import stdin

"https://www.acmicpc.net/problem/1931 회의실 배정 <Silver II>"

num_of_meeting = int(stdin.readline())
meetings = dict()

for _ in range(num_of_meeting):
    start, end = tuple(map(int, stdin.readline().split()))
    if meetings.get(start) is None:
        meetings[start] = end

table = []
end_of_table = max(meetings.keys())

for i in sorted(meetings.keys()):
    result = 1
    start = i
    end = meetings[start]

    while start < end_of_table:
        start = end+1
        while meetings.get(start) is None and start < end_of_table:
            start += 1

        try:
            end = meetings[start]
            result += 1
        except KeyError:
            pass

    table.append(result)

print(max(table))
