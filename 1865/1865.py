from sys import stdin, maxsize

def bellman_ford_minus_cycle(graph, num_of_vertex, start):
    distances = [maxsize for _ in range(num_of_vertex)]
    snapshot = []

    for i in range(2):
        if i == 1:
            snapshot.extend(distances)
        for v in range(num_of_vertex):
            for t in range(num_of_vertex):
                if graph[v][t] != maxsize:
                    distances[t] = min(
                        distances[t], distances[v] + graph[v][t]
                    )

    validate = True
    if distances[0] != snapshot[0]:
        validate = False
    
    return validate

def graph_init(num_of_vertex):
    graph = [
        [maxsize for _ in range(num_of_vertex)]
        for _ in range(num_of_vertex)
    ]

    return graph

def graph_add_line(graph, src, dst, cost):
    graph[src][dst] = cost

def solve_wormhole(num_of_area, num_of_road, num_of_wormhole):
    graph = graph_init(num_of_area)
    input_line = lambda: map(lambda a:int(a)-1, stdin.readline().split())

    for i in range(num_of_road + num_of_wormhole):
        src, dst, cost = input_line()
        cost += 1
        if i >= num_of_road:
            cost = -cost

        graph_add_line(graph, src, dst, cost)

    result = bellman_ford_minus_cycle(graph, num_of_area, 0)
    if not result:
        print("YES")
    else:
        print("NO")

num_of_case = int(stdin.readline())
for _ in range(num_of_case):
    line = map(int, stdin.readline().split())
    num_of_area, num_of_road, num_of_wormhole = line
    solve_wormhole(num_of_area, num_of_road, num_of_wormhole)

