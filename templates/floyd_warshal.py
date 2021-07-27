from sys import stdin, maxsize

class MatrixGraph:
    def __init__(
        self,
        num_of_vertex,
        is_bidirection=False,
        is_zero_index=True):
        self.num_of_vertex = num_of_vertex
        self.matrix = [
            [maxsize for _ in range(num_of_vertex)]
            for _ in range(num_of_vertex)
        ]
        for vertex in range(num_of_vertex):
            self.matrix[vertex][vertex] = 0

        self.is_bidirection = is_bidirection
        self.is_zero_index = is_zero_index

    def add_line(self, src, dest, cost):
        if not self.is_zero_index:
            src -= 1
            dest -= 1

        if self.matrix[src][dest] > cost:
            self.matrix[src][dest] = cost
        if self.is_bidirection and self.matrix[dest][src] > cost:
            self.matrix[dest][src] = cost

def floyd_warshal(graph):
    num_of_vertex = graph.num_of_vertex
    matrix = graph.matrix

    for k in range(num_of_vertex):
        for i in range(num_of_vertex):
            for j in range(num_of_vertex):
                predict_cost = matrix[i][k] + matrix[k][j]
                if matrix[i][j] > predict_cost:
                    matrix[i][j] = predict_cost

    return matrix

num_of_vertex = int(stdin.readline())
num_of_line = int(stdin.readline())
graph = MatrixGraph(num_of_vertex, is_zero_index=False)

for _ in range(num_of_line):
    src, dest, cost = map(int, stdin.readline().split())
    graph.add_line(src, dest, cost)

matrix = floyd_warshal(graph)

for vertex in matrix:
    for cost in vertex:
        if cost == maxsize:
            cost = 0
        print(cost, end=' ')
    print()

