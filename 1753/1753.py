from sys import stdin
from collections import deque

"https://www.acmicpc.net/problem/1753 최단경로 <Gold V>"

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

class WeightedGraph(Graph):
    def __init__(self,num_of_vertex,is_zero_index=False):
        super().__init__(num_of_vertex, False, is_zero_index)
        self.weight = [[] for _ in range(num_of_vertex)]

    def add_line(self, src, dest, cost):
        if not self.is_zero_index:
            src -= 1
            dest -= 1
        self.vertex[src].append(dest)
        self.weight[src].append(cost)

    def get_weight_list(self):
        return self.weight

def dijkstra(graph, start):
    vertex_list = graph.get_vertex_list()
    weight_list = graph.get_weight_list()
    queue = deque()
    num_of_vertex = graph.get_num_of_vertex()
    distance = [None for _ in range(num_of_vertex)]

    queue.append(start)
    distance[start] = 0
    
    while queue:
        cur = queue.popleft()
        current_distance = distance[cur]

        for next, weight in zip(vertex_list[cur], weight_list[cur]):
            next_distance = distance[next]
            predict_distance = current_distance + weight
            if not next_distance or predict_distance < next_distance:
                distance[next] = predict_distance
                queue.append(next)

    return distance

num_of_vertex, num_of_line = map(int,stdin.readline().split())
graph = WeightedGraph(num_of_vertex, False)
start = int(stdin.readline()) - 1

for _ in range(num_of_line):
    src, dest, cost = map(int, stdin.readline().split())
    graph.add_line(src, dest, cost)

result = dijkstra(graph, start)

for d in result:
    if d is None:
        d = "INF"
    print(d)

