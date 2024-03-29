from sys import stdin, maxsize

"https://www.acmicpc.net/problem/1865 웜홀 <Gold IV>"

class Edge:
    def __init__(self, src, dst, weight):
        self.source = src - 1
        self.destination = dst - 1
        self.weight = weight

def BellmanFord(edges, num_of_edge, num_of_node, source):
    distance = [maxsize if i != source else 0 for i in range(num_of_node)]

    for node in range(num_of_node):
        for e in edges:
            relaxing = distance[e.source] + e.weight
            if relaxing < distance[e.destination]:
                distance[e.destination] = relaxing
                if node == num_of_node - 1:
                    return True

    return False

def input_integers():
    return map(int, stdin.readline().split())

def input_edges(num_of_edge, is_negative=False, is_bidirection=False):
    edges = []
    for _ in range(num_of_edge):
        src, dst, weight = input_integers()
        if is_negative:
            weight = -weight

        edges.append(Edge(src, dst, weight))
        if is_bidirection:
            edges.append(Edge(dst, src, weight))

    return edges

num_of_case = int(stdin.readline())
for _ in range(num_of_case):
    num_of_node, num_of_road, num_of_wormhole = input_integers()
    edges = []

    edges.extend(input_edges(num_of_road, is_bidirection=True))
    edges.extend(input_edges(num_of_wormhole, is_negative=True))
    if BellmanFord(edges, num_of_road + num_of_wormhole, num_of_node, 0):
        print("YES")
    else:
        print("NO")
