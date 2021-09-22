from functools import reduce

def solution(numbers):
    numbers = [str(v) for v in numbers]
    max_len = len(max(numbers, key=len))
    numbers = sorted(
        numbers,key=lambda v: v + v[-1] * (max_len - len(v)),reverse=True
    )
    answer = ''.join(numbers)
    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([5, 56, 54, 1200, 12]))
