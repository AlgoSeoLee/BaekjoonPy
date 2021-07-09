from sys import stdin

"https://www.acmicpc.net/problem/1167 트리의 지름 <Gold III>"

class Graph:
    def __init__(
        self,
        num_of_vertex,
        is_bidirection = True,
        is_zero_index = False
    ):
        self.num_of_vertex = num_of_vertex
        self.vertex = [[] for _ in range(num_of_vertex)]
        self.is_bidirection = is_bidirection
        self.is_zero_index = is_zero_index

    def add_line(self, src, dest, distance):
        if not self.is_zero_index:
            src -= 1
            dest -= 1

        self.vertex[src].append((dest, distance))
        if self.is_bidirection:
            self.vertex[dest].append((src, distance))

    def get_vertex_list(self):
        return self.vertex

    def get_num_of_vertex(self):
        return self.num_of_vertex

def DFS(graph, start):
    vertex_list = graph.get_vertex_list()
    stack = []
    num_of_vertex = graph.get_num_of_vertex()
    visited = [False for _ in range(num_of_vertex)]
    result = {}

    stack.append((start, 0))
    visited[start] = True
    
    while stack: 
        cur, dist = stack.pop()
        for n,d in vertex_list[cur]:
            if not visited[n]:
                visited[n] = True
                sum_dist = d + dist
                stack.append((n, sum_dist))
                same_dist = result.get(sum_dist)
                if not same_dist:
                    result[sum_dist] = [n]
                else:
                    same_dist.append(n)

    maximum = max(result.keys())
    return result[maximum][0], maximum

num_of_vertex = int(stdin.readline())
graph = Graph(num_of_vertex,is_bidirection=False)
for _ in range(num_of_vertex):
    line = list(map(int, stdin.readline().split()[:-1]))
    src = line[0]
    line = line[1:]
    len_line = len(line)
    for d, c in zip(range(0,len_line,2), range(1,len_line,2)):
        dest = line[d]
        cost = line[c]
        graph.add_line(src, dest, cost)

far, _ = DFS(graph, 0)
_, dist = DFS(graph, far)
print(dist)
