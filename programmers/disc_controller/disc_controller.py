from heapq import heapify, heappush, heappop

def solution(jobs):
    answer = 0
    
    tasks = list(map(lambda j: tuple(j), jobs))
    heapify(tasks)

    sec = 0
    waiting_time = []
    scheduler = []

    while tasks or scheduler:
        while tasks:
            t = tasks[0]
            t_req, _ = t

            if sec >= t_req:
                heappop(tasks)
                heappush(scheduler, tuple(reversed(t)))
            else:
                break

        if scheduler:
            t_exe, t_req = heappop(scheduler)
            sec += t_exe
            waiting_time.append(sec - t_req)
        else:
            sec += 1

    answer = sum(waiting_time) // len(waiting_time)
    
    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
