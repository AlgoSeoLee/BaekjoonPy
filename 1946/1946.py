from sys import stdin, maxsize

"https://www.acmicpc.net/problem/1946 신입 사원 <Silver I>"

num_of_case = int(stdin.readline())
for _ in range(num_of_case):
    num_of_register = int(stdin.readline())
    registers = []
    for _ in range(num_of_register):
        registers.append(tuple(map(int, stdin.readline().split())))

    registers.sort()
    answer = 0
    interview_lowest = maxsize
    for _, interview in registers:
        if interview <= interview_lowest:
            interview_lowest = interview
            answer += 1

    print(answer)

