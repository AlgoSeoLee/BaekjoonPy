from sys import stdin
from collections import deque

"https://www.acmicpc.net/problem/11725 트리의 부모 찾기 <Silver II>"

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

    result = [0 for _ in range(num_of_vertex)]
    queue.append(start)
    visited[start] = True
    
    while queue:
        cur = queue.popleft()

        for next in vertex_list[cur]:
            is_visited = visited[next]
            if not is_visited:
                result[next] = cur + 1
                visited[next] = True
                queue.append(next)

    return result

num_of_vertex = int(stdin.readline())
graph = Graph(num_of_vertex)
for src in range(num_of_vertex - 1):
    src, dst = map(int, stdin.readline().split())
    graph.add_line(src, dst)

result = BFS(graph, 0)

for root in result[1:]:
    print(root) 

