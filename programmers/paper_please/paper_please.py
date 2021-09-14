
MAXIMUM = 987654321987654321

def solution(n, times):
    answer = MAXIMUM
    times.sort()

    start = 1
    end = n * max(times)
    while start <= end:
        mid = (start + end) // 2
        process = 0

        for t in times:
            process += mid // t

        if process >= n:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1

    return answer

print(solution(6, [7, 10]))
