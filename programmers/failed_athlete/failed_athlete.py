
def solution(participant, completion):
    completion_times = {}
    for name in completion:
        times = completion_times.get(name)
        if not times:
            times = 0

        completion_times[name] = times + 1

    for name in participant:
        if completion_times.get(name):
            completion_times[name] -= 1
        else:
            return name
