from sys import stdin
from collections import deque

def BFS(start, target):
    queue = deque()
    visited = {}

    queue.append((start, 1))
    visited[start] = True

    try:
        while True:
            current, level = queue.popleft()
    
            next_steps = [
                current * 2,
                current * 10 + 1
            ]
    
            next_level = level + 1
            for step in next_steps:
                if step == target:
                    return next_level
                elif not visited.get(step): 
                    if step > target:
                        continue
                    visited[step] = True
                    queue.append((step, next_level))
    except IndexError:
        return -1

start, target = map(int, stdin.readline().split())
print(BFS(start, target))
