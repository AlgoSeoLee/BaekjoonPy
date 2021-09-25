from sys import stdin
from collections import deque

"https://www.acmicpc.net/problem/1325 효율적인 해킹 <Silver II>"

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
    visited = [False for _ in range(num_of_vertex)]

    queue.append(start)
    visited[start] = True
    hacking = 0
    
    while queue:
        cur = queue.popleft()

        for next in vertex_list[cur]:
            if not visited[next]:
                hacking += 1
                visited[next] = True
                queue.append(next)

    return hacking

num_of_vertex, num_of_line = map(int, stdin.readline().split())
graph = Graph(num_of_vertex, False, False)

for _ in range(num_of_line):
    dst, src = map(int, stdin.readline().split())
    graph.add_line(src, dst)

maximum_depth = 0
maximum_depth_starts = []
for start in range(num_of_vertex):
    depth = BFS(graph, start)
    if depth > maximum_depth:
        maximum_depth = depth
        maximum_depth_starts = [start + 1]
    elif depth == maximum_depth:
        maximum_depth_starts.append(start + 1)

print(*maximum_depth_starts)
