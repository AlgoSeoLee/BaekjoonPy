from sys import stdin, maxsize

def compare_register(registers, primary_key, sub_key, score_limit=maxsize):
    result = 0
    delete = []
    for reg in registers:
        score = sub_key(reg)
        if score <= score_limit:
            result += 1
            delete.append(reg)
            score_limit = score

    for reg in delete:
        registers.remove(reg)

    return result, score_limit

num_of_case = int(stdin.readline())
for _ in range(num_of_case):
    num_of_register = int(stdin.readline())
    registers = []
    for _ in range(num_of_register):
        written, interview = map(int, stdin.readline().split())
        registers.append((written, interview))

    registers.sort()
    written_key = lambda v: v[0]
    interview_key = lambda v: v[1]
    result, interview_limit = compare_register(
        registers, written_key, interview_key
    )
    interview_result, _ = compare_register(
        registers, interview_key, written_key, interview_limit
    )
    result += interview_result

    print(result)

