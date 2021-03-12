from sys import stdin, setrecursionlimit

"https://www.acmicpc.net/problem/11724 연결 요소의 개수 <Silver II>"

def _DFS(vertex, visited, N):
    visited[N] = True
    for i in vertex[N]:
        if not visited[i]:
            _DFS(vertex, visited, i)

def TotalConnectComponent(vertex):
    visited = []

    number_of_vertex = len(vertex)
    for _ in range(number_of_vertex):
        visited.append(False)
    
    component = 0
    for i in range(number_of_vertex):
        if visited[i]:
            continue

        _DFS(vertex, visited, i)
        component += 1

    return component

def GetNumbers():
    return map(int, stdin.readline().split())

setrecursionlimit(10**6)

number_of_vertex, number_of_line = GetNumbers()

vertex = []
for _ in range(number_of_vertex):
    vertex.append([])

for _ in range(number_of_line):
    x, y = map(lambda n: n - 1, GetNumbers())

    vertex[x].append(y)
    vertex[y].append(x)

print(TotalConnectComponent(vertex))
