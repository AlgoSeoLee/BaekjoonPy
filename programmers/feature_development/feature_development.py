from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    num_of_feature = len(progresses)

    while progresses:
        for i, s in zip(range(num_of_feature), speeds):
            progresses[i] += s

        deploy = 0
        while progresses:
            if progresses[0] >= 100:
                deploy += 1
                progresses.popleft()
                speeds.popleft()
            else:
                break

        if deploy:
            answer.append(deploy)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
