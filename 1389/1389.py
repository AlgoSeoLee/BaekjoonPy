from sys import stdin
from collections import deque

"https://www.acmicpc.net/problem/1389 케빈 베이컨의 6단계 법칙 <Silver I>"

class Graph:
    def __init__(self, num_of_vertex, is_bidirection = True, is_zero_index = False):
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
    visited = [-1 for _ in range(num_of_vertex)]

    queue.append((start, 0))
    visited[start] = 0
    
    try:
        while True:
            cur, level = queue.popleft()
            level += 1

            for next in vertex_list[cur]:
                target_level = visited[next]
                if level < target_level or target_level == -1:
                    visited[next] = level
                    queue.append((next, level))
    except IndexError:
        pass

    score = 0
    for level in visited:
        if level != -1:
            score += level

    return score

def game(graph):
    num_of_vertex = graph.get_num_of_vertex()
    minimum_level = 50001
    minimum_target = 0

    for i in range(num_of_vertex):
        result = BFS(graph, i)
        if result < minimum_level:
            minimum_level = result
            minimum_target = i

    return minimum_target + 1

num_of_users, num_of_relationship = map(int, stdin.readline().split())
graph = Graph(num_of_users)
for _ in range(num_of_relationship):
    src, dest = map(int, stdin.readline().split())
    graph.add_line(src, dest)

print(game(graph))
