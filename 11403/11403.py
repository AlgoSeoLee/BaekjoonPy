from sys import stdin
from collections import deque

class Graph:
    def __init__(
        self,
        num_of_vertex, is_bidirection = True,
        is_zero_index = False
    ):
        self.num_of_vertex = num_of_vertex
        self.vertex = [[] for _ in range(num_of_vertex)]
        self.is_bidirection = is_bidirection
        self.is_zero_index = is_zero_index

    def add_line(self, src, dest):
        if not self.is_zero_index:
            src -= 1
            dest -= 1

        self.vertex[src].append(dest)
        if self.is_bidirection:
            self.vertex[dest].append(src)

    def get_vertex_list(self):
        return self.vertex

    def get_num_of_vertex(self):
        return self.num_of_vertex

def BFS(graph, start):
    vertex_list = graph.get_vertex_list()
    queue = deque()
    num_of_vertex = graph.get_num_of_vertex()
    visited = [0 for _ in range(num_of_vertex)]

    queue.append(start)
    
    while queue:
        cur = queue.popleft()

        for next in vertex_list[cur]:
            is_visited = visited[next]
            if is_visited == 0:
                visited[next] = 1
                queue.append(next)

    return visited

num_of_vertex = int(stdin.readline())
graph = Graph(num_of_vertex, False, True)
for src in range(num_of_vertex):
    lines = map(
        lambda x: x == '1',
        stdin.readline().split()
    )
    for line in zip(lines, range(num_of_vertex)):
        is_line, dest = line
        if is_line :
            graph.add_line(src, dest)

for start in range(num_of_vertex):
    for vertex in BFS(graph, start):
        print(vertex, end=' ')
    print()

