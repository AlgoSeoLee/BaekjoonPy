from sys import stdin, maxsize
from heapq import heappop, heappush

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
    def __init__(
        self,
        num_of_vertex,
        is_bidirection=False,
        is_zero_index=False):
        super().__init__(
            num_of_vertex,
            is_bidirection,
            is_zero_index
        )
        self.weight = [[] for _ in range(num_of_vertex)]

    def add_line(self, src, dest, cost):
        if not self.is_zero_index:
            src -= 1
            dest -= 1
        self.vertex[src].append(dest)
        self.weight[src].append(cost)
        if self.is_bidirection:
            self.vertex[dest].append(src)
            self.weight[dest].append(cost)

    def get_weight_list(self):
        return self.weight

def dijkstra(graph, start):
    vertex_list = graph.get_vertex_list()
    weight_list = graph.get_weight_list()
    num_of_vertex = graph.get_num_of_vertex()

    queue = []
    distances = [maxsize for _ in range(num_of_vertex)]

    queue.append((0, start))
    distances[start] = 0
    
    while queue:
        cost, cur = heappop(queue)
        current_distance = distances[cur]
        if cost > current_distance:
            continue

        for next, weight in zip(vertex_list[cur], weight_list[cur]):
            next_distance = distances[next]
            predict_distance = current_distance + weight
            if predict_distance < next_distance:
                distances[next] = predict_distance
                heappush(queue,(predict_distance, next))

    return distances

num_of_vertex, num_of_line = map(int,stdin.readline().split())
graph = WeightedGraph(num_of_vertex, False)
start = int(stdin.readline()) - 1

for _ in range(num_of_line):
    src, dest, cost = map(int, stdin.readline().split())
    graph.add_line(src, dest, cost)

result = dijkstra(graph, start)

for d in result:
    if d == maxsize:
        d = "INF"
    print(d)

