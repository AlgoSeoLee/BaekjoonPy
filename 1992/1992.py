from sys import stdin

"https://www.acmicpc.net/problem/1992 쿼드트리 <Silver I>"

dispense_data = lambda x: 1 if x == '1' else 0

def generate_quad_tree(data, size):
    data_pool = set()
    is_same = True
    for line in data:
        data_pool = data_pool.union(set(line))
        if len(data_pool) != 1:
            is_same = False
            break

    if is_same:
        return data_pool.pop()

    half = size // 2
    result = '('
    for start_y in range(0, size, half):
        split_by_y = data[start_y:start_y+half]
        for start_x in range(0, size, half):
            quad = list(
                map(lambda line: line[start_x:start_x+half], split_by_y))
            result += str(generate_quad_tree(quad, half))

    return result + ')'

size = int(stdin.readline())
data = [
    list(map(dispense_data, stdin.readline().rstrip())) for _ in range(size)]

print(generate_quad_tree(data, size))

